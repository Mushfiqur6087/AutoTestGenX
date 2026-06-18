import asyncio
import json
import os
import time
from datetime import datetime
from typing import Any, Dict, List, Optional

from test_generation.framework.orchestrator.reporters import _render_critique_md, _render_workflow_critique_md, _render_test_cases_md
from test_generation.framework.agents.base import BaseAgent
from test_generation.framework.agents.structural_model_validator import StructuralModelValidatorAgent
from test_generation.framework.agents.edge_test_case_generator import EdgeTestCaseGeneratorAgent
from test_generation.framework.agents.negative_test_case_generator import NegativeTestCaseGeneratorAgent
from test_generation.framework.agents.positive_test_case_generator import PositiveTestCaseGeneratorAgent
from test_generation.framework.agents.structural_model_generator import StructuralModelGeneratorAgent
from test_generation.framework.agents.workflow_validator import WorkflowValidatorAgent
from test_generation.framework.agents.workflow_extractor import WorkflowExtractorAgent
from test_generation.framework.orchestrator.state import PipelineState

MAX_ATTEMPTS = 3


def _module_debug_dir(state: PipelineState, module_title: str) -> str:
    """Return a per-module debug subdirectory path, creating it on demand. Empty string when debug is off."""
    debug: bool = state.get("debug", False)
    debug_dir: str = state.get("debug_dir", "")
    if not (debug and debug_dir):
        return ""
    slug = module_title.replace(" ", "_")
    path = os.path.join(debug_dir, slug)
    os.makedirs(path, exist_ok=True)
    return path


def _agent_kwargs(state: PipelineState, stage_file: str, module_debug_dir: str = "") -> dict:
    debug: bool = state.get("debug", False)
    if debug and module_debug_dir:
        debug_file = os.path.join(module_debug_dir, stage_file)
        BaseAgent.init_debug_session(debug_file, state["model"])
    else:
        debug_file = state.get("debug_file", "debug_log.txt")
    return dict(api_key=state["api_key"], model=state["model"], debug=debug, debug_file=debug_file)


async def generate_and_critique_node(state: PipelineState) -> Dict[str, Any]:
    t0 = time.time()
    modules = state["functional_desc"].get("modules", [])
    desc_by_id = {m["id"]: m["description"] for m in modules}

    print(f"\n[1/4] Generating Structural Model with critic-guided retry ({len(modules)} module(s))...")

    async def _process_module(module: Dict[str, Any]) -> Dict[str, Any]:
        module_dir = _module_debug_dir(state, module["title"])
        ast_agent = StructuralModelGeneratorAgent(**_agent_kwargs(state, "01_structural_model.log", module_dir))
        critic_agent = StructuralModelValidatorAgent(**_agent_kwargs(state, "02_structural_model_validator.log", module_dir))
        desc = desc_by_id.get(module["id"], "")
        fixes: List[str] = []
        ast: Dict[str, Any] = {}
        critique: Dict[str, Any] = {}

        for attempt in range(MAX_ATTEMPTS):
            label = f"attempt {attempt + 1}/{MAX_ATTEMPTS}"

            ast = await ast_agent.arun(module, fixes=fixes if fixes else None)

            critique = await critic_agent.arun(desc, ast)
            verdict = critique.get("verdict", "retry")

            if verdict == "yes":
                n = len(ast.get("components", {}))
                print(f"  OK {module['title']} | {label} | {n} component(s)")
                return {"ast": ast, "critique": critique, "attempts": attempt + 1}

            fixes = critique.get("fixes", [])
            missing = len(critique.get("missing", []))
            phantoms = len(critique.get("phantoms", []))

            if attempt < MAX_ATTEMPTS - 1:
                print(
                    f"  ~~ {module['title']} | {label} | verdict=retry"
                    f" | missing={missing} phantoms={phantoms} | retrying..."
                )
            else:
                print(
                    f"  !! {module['title']} | max attempts reached"
                    f" | missing={missing} phantoms={phantoms} | shipping final attempt"
                )

        return {"ast": ast, "critique": critique, "attempts": MAX_ATTEMPTS, "forced_ship": True}

    raw = await asyncio.gather(*[_process_module(m) for m in modules], return_exceptions=True)

    structural_model_results = []
    structural_model_critique_results = []

    for module, r in zip(modules, raw):
        if isinstance(r, Exception):
            print(f"  !! Failed for {module['title']}: {r}")
            structural_model_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "error": str(r),
                "ast": {},
            })
            structural_model_critique_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "critique": None,
                "error": str(r),
            })
        else:
            structural_model_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "ast": r["ast"],
                "attempts": r["attempts"],
            })
            structural_model_critique_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "critique": r["critique"],
                "forced_ship": r.get("forced_ship", False),
            })

    print(f"  Done in {time.time() - t0:.1f}s")
    return {
        "structural_model_results": structural_model_results,
        "structural_model_critique_results": structural_model_critique_results,
    }


async def extract_workflows_node(state: PipelineState) -> Dict[str, Any]:
    t0 = time.time()
    modules = state["functional_desc"].get("modules", [])
    structural_model_results = state.get("structural_model_results", [])

    ast_by_id = {r["module_id"]: r.get("ast", {}) for r in structural_model_results}
    desc_by_id = {m["id"]: m["description"] for m in modules}

    # Only extract workflows for modules that have a valid AST
    runnable = [m for m in modules if ast_by_id.get(m["id"])]

    print(f"\n[2/4] Extracting & critiquing workflows ({len(runnable)} module(s))...")

    async def _extract_module(module: Dict[str, Any]) -> Dict[str, Any]:
        module_dir = _module_debug_dir(state, module["title"])
        extractor = WorkflowExtractorAgent(**_agent_kwargs(state, "02b_workflow_extractor.log", module_dir))
        critic = WorkflowValidatorAgent(**_agent_kwargs(state, "02c_workflow_validator.log", module_dir))
        desc = desc_by_id.get(module["id"], "")
        ast = ast_by_id[module["id"]]
        fixes: List[str] = []
        workflows: List[Dict[str, Any]] = []
        critique: Dict[str, Any] = {}

        for attempt in range(MAX_ATTEMPTS):
            label = f"attempt {attempt + 1}/{MAX_ATTEMPTS}"

            result = await extractor.arun(module["title"], ast, desc, fixes=fixes if fixes else None)
            workflows = result.get("workflows", [])

            critique = await critic.arun(desc, ast, workflows)
            verdict = critique.get("verdict", "retry")

            if verdict == "yes":
                print(f"  OK {module['title']} | {label} | {len(workflows)} workflow(s)")
                return {"workflows": workflows, "critique": critique, "attempts": attempt + 1}

            fixes = critique.get("fixes", [])
            missing = len(critique.get("missing", []))
            phantoms = len(critique.get("phantoms", []))

            if attempt < MAX_ATTEMPTS - 1:
                print(
                    f"  ~~ {module['title']} | {label} | verdict=retry"
                    f" | missing={missing} phantoms={phantoms} | retrying..."
                )
            else:
                print(
                    f"  !! {module['title']} | max attempts reached"
                    f" | missing={missing} phantoms={phantoms} | shipping final attempt"
                )

        return {"workflows": workflows, "critique": critique, "attempts": MAX_ATTEMPTS, "forced_ship": True}

    raw = await asyncio.gather(*[_extract_module(m) for m in runnable], return_exceptions=True)

    workflow_results = []
    workflow_critique_results = []

    for module, r in zip(runnable, raw):
        if isinstance(r, Exception):
            print(f"  !! Workflow extraction failed for {module['title']}: {r}")
            workflow_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "workflows": [],
                "error": str(r),
            })
            workflow_critique_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "critique": None,
                "error": str(r),
            })
        else:
            workflow_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "workflows": r["workflows"],
                "attempts": r["attempts"],
            })
            workflow_critique_results.append({
                "module_id": module["id"],
                "module_title": module["title"],
                "critique": r["critique"],
                "forced_ship": r.get("forced_ship", False),
            })

    print(f"  Done in {time.time() - t0:.1f}s")
    return {
        "workflow_results": workflow_results,
        "workflow_critique_results": workflow_critique_results,
    }


async def generate_tests_node(state: PipelineState) -> Dict[str, Any]:
    t0 = time.time()
    modules = state["functional_desc"].get("modules", [])
    structural_model_results = state.get("structural_model_results", [])
    workflow_results = state.get("workflow_results") or []

    ast_by_id = {r["module_id"]: r.get("ast", {}) for r in structural_model_results}
    desc_by_id = {m["id"]: m["description"] for m in modules}
    workflows_by_id = {r["module_id"]: r.get("workflows", []) for r in workflow_results}

    test_types = state.get("test_types") or {"positive", "negative", "edge"}

    # Skip modules that failed AST generation (empty ast)
    runnable = [m for m in modules if ast_by_id.get(m["id"])]
    skipped = len(modules) - len(runnable)

    total_calls = len(runnable) * len(test_types)
    type_label = "/".join(sorted(test_types))
    print(f"\n[3/4] Generating test cases ({total_calls} calls across {len(runnable)} module(s), types: {type_label})...")
    if skipped:
        print(f"  Skipping {skipped} module(s) with no AST.")

    async def _process_module(module: Dict[str, Any]) -> Dict[str, Any]:
        title = module["title"]
        ast = ast_by_id[module["id"]]
        desc = desc_by_id.get(module["id"], "")
        workflows = workflows_by_id.get(module["id"], [])
        module_dir = _module_debug_dir(state, title)

        async def _run_if(agent_cls, log_file, type_name):
            if type_name not in test_types:
                return None
            agent = agent_cls(**_agent_kwargs(state, log_file, module_dir))
            return await agent.arun(title, ast, desc, workflows=workflows)

        pos, neg, edge = await asyncio.gather(
            _run_if(PositiveTestCaseGeneratorAgent, "03_positive_test_case_generator.log", "positive"),
            _run_if(NegativeTestCaseGeneratorAgent, "04_negative_test_case_generator.log", "negative"),
            _run_if(EdgeTestCaseGeneratorAgent, "05_edge_test_case_generator.log", "edge"),
            return_exceptions=True,
        )

        merged = _merge_module_tests(title, pos, neg, edge)
        total = merged["summary"]["total"]
        print(f"  OK {title} | {total} test(s) (pos={merged['summary']['positive']} neg={merged['summary']['negative']} edge={merged['summary']['boundary'] + merged['summary']['edge']})")
        return merged

    raw = await asyncio.gather(*[_process_module(m) for m in runnable], return_exceptions=True)

    test_results = []
    for module, r in zip(runnable, raw):
        if isinstance(r, Exception):
            print(f"  !! Failed for {module['title']}: {r}")
            test_results.append({
                "module": module["title"],
                "error": str(r),
                "test_cases": [],
                "summary": {"total": 0, "positive": 0, "negative": 0, "boundary": 0, "edge": 0,
                            "high_priority": 0, "medium_priority": 0, "low_priority": 0},
            })
        else:
            test_results.append(r)

    print(f"  Done in {time.time() - t0:.1f}s")
    return {"test_results": test_results}


def _merge_module_tests(
    module_title: str,
    positive: Any,
    negative: Any,
    edge: Any,
) -> Dict[str, Any]:
    def _safe_cases(result: Any, category: str) -> List[Dict[str, Any]]:
        if isinstance(result, Exception) or not isinstance(result, dict):
            return []
        cases = result.get("test_cases", [])
        for c in cases:
            c["category"] = category
        return cases

    pos_cases = _safe_cases(positive, "positive")
    neg_cases = _safe_cases(negative, "negative")
    edge_cases = _safe_cases(edge, "edge")
    all_cases = pos_cases + neg_cases + edge_cases

    # Renumber TCs sequentially across all categories
    for i, tc in enumerate(all_cases, 1):
        tc["tc_id"] = f"TC-{i:03d}"

    def _count(cases: List, priority: str) -> int:
        return sum(1 for c in cases if c.get("priority") == priority)

    edge_summary = edge.get("summary", {}) if isinstance(edge, dict) else {}

    return {
        "module": module_title,
        "test_cases": all_cases,
        "summary": {
            "total": len(all_cases),
            "positive": len(pos_cases),
            "negative": len(neg_cases),
            "edge": len(edge_cases),          # actual edge TC count, not from agent summary
            "boundary": edge_summary.get("boundary", 0),
            "input_edge": edge_summary.get("input_edge", 0),
            "interaction_edge": edge_summary.get("interaction_edge", 0),
            "state_edge": edge_summary.get("state_edge", 0),
            "data_edge": edge_summary.get("data_edge", 0),
            "high_priority": _count(all_cases, "high"),
            "medium_priority": _count(all_cases, "medium"),
            "low_priority": _count(all_cases, "low"),
        },
    }


def finalize_node(state: PipelineState) -> Dict[str, Any]:
    t0 = time.time()
    print("\n[4/4] Saving output...")

    output_dir = state["output_dir"]
    functional_desc = state["functional_desc"]

    output = {
        "project_name": functional_desc.get("project_name", ""),
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "modules": state.get("structural_model_results", []),
    }

    structural_model_path = os.path.join(output_dir, "structural-model.json")
    with open(structural_model_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"  Saved Structural Model to:       {structural_model_path}")

    project_slug = output.get("project_name", "output").replace(" ", "-")
    model_slug = state.get("model", "").replace("/", "-")

    critique_results = state.get("structural_model_critique_results")
    if critique_results is not None:
        critique_output = {
            "project_name": functional_desc.get("project_name", ""),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "modules": critique_results,
        }
        critique_path = os.path.join(output_dir, "structural-model-critique.json")
        with open(critique_path, "w", encoding="utf-8") as f:
            json.dump(critique_output, f, indent=2)
        print(f"  Saved critique to:     {critique_path}")

        critique_md_path = os.path.join(output_dir, f"{project_slug}-{model_slug}-critique.md")
        with open(critique_md_path, "w", encoding="utf-8") as f:
            f.write(_render_critique_md(critique_output))
        print(f"  Saved critique (md):   {critique_md_path}")

    test_results = state.get("test_results")
    if test_results is not None:
        total_tests = sum(r.get("summary", {}).get("total", 0) for r in test_results)
        tests_output = {
            "project_name": functional_desc.get("project_name", ""),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "model": state.get("model", ""),
            "modules": test_results,
            "total_summary": {
                "total_modules": len(test_results),
                "total_tests": total_tests,
                "positive": sum(r.get("summary", {}).get("positive", 0) for r in test_results),
                "negative": sum(r.get("summary", {}).get("negative", 0) for r in test_results),
                "boundary": sum(r.get("summary", {}).get("boundary", 0) for r in test_results),
                "edge": sum(r.get("summary", {}).get("edge", 0) for r in test_results),
                "high_priority": sum(r.get("summary", {}).get("high_priority", 0) for r in test_results),
                "medium_priority": sum(r.get("summary", {}).get("medium_priority", 0) for r in test_results),
                "low_priority": sum(r.get("summary", {}).get("low_priority", 0) for r in test_results),
            },
        }
        tests_path = os.path.join(output_dir, "test-cases.json")
        with open(tests_path, "w", encoding="utf-8") as f:
            json.dump(tests_output, f, indent=2)
        print(f"  Saved test cases to:   {tests_path}  ({total_tests} total)")

        results_dir = os.path.join("results", project_slug, model_slug)
        os.makedirs(results_dir, exist_ok=True)
        tests_md_path = os.path.join(results_dir, f"{project_slug}-tests.md")
        with open(tests_md_path, "w", encoding="utf-8") as f:
            f.write(_render_test_cases_md(tests_output))
        print(f"  Saved test cases (md): {tests_md_path}")

        modules_dir = os.path.join(results_dir, "modules")
        os.makedirs(modules_dir, exist_ok=True)
        for module in test_results:
            module_name = module.get("module", "Unknown").replace(" ", "_")
            module_md_path = os.path.join(modules_dir, f"{module_name}.md")
            single_module_data = {
                "project_name": functional_desc.get("project_name", ""),
                "generated_at": tests_output.get("generated_at"),
                "model": tests_output.get("model"),
                "modules": [module]
            }
            with open(module_md_path, "w", encoding="utf-8") as f:
                f.write(_render_test_cases_md(single_module_data))

    workflow_results = state.get("workflow_results")
    if workflow_results is not None:
        workflows_output = {
            "project_name": functional_desc.get("project_name", ""),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "modules": workflow_results,
        }
        workflows_path = os.path.join(output_dir, "workflows.json")
        with open(workflows_path, "w", encoding="utf-8") as f:
            json.dump(workflows_output, f, indent=2)
        total_wf = sum(len(r.get("workflows", [])) for r in workflow_results)
        print(f"  Saved workflows to:    {workflows_path}  ({total_wf} total)")

    workflow_critique_results = state.get("workflow_critique_results")
    if workflow_critique_results is not None:
        wf_critique_output = {
            "project_name": functional_desc.get("project_name", ""),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "modules": workflow_critique_results,
        }
        wf_critique_path = os.path.join(output_dir, "workflow-validator-critique.json")
        with open(wf_critique_path, "w", encoding="utf-8") as f:
            json.dump(wf_critique_output, f, indent=2)
        print(f"  Saved wf-critique to:  {wf_critique_path}")

        wf_critique_md_path = os.path.join(output_dir, f"{project_slug}-{model_slug}-workflow-validator-critique.md")
        with open(wf_critique_md_path, "w", encoding="utf-8") as f:
            f.write(_render_workflow_critique_md(wf_critique_output))
        print(f"  Saved wf-critique(md): {wf_critique_md_path}")

    print(f"  Done in {time.time() - t0:.1f}s")
    return {"output": output}


