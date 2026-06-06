#!/usr/bin/env python3
"""
Test Case Generation CLI — Structural Model generation from functional specifications.

Usage:
    test_case_generation --generate --input spec.md --api-key "sk-..." --model openai/gpt-4o-mini
"""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional

import test_case_generation
from test_case_generation.framework.agents.base import set_max_concurrency
from test_case_generation.framework.orchestrator.generator import UIASTGenerator
from test_case_generation.framework.orchestrator.runs import (
    make_run_id,
    make_run_metadata,
    read_sidecar,
    write_sidecar,
)
from test_case_generation.framework.orchestrator.post_verification_generator import PostVerificationGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Test Case Generation — Structural Model generation from functional specifications"
    )
    parser.add_argument("--version", action="version", version=f"test_case_generation {test_case_generation.__version__}")
    parser.add_argument("--generate", action="store_true", help="Generate Structural Model from spec")
    parser.add_argument("--post-verify", action="store_true", help="Run the post-verification pipeline")
    parser.add_argument("--test-cases", help="Path to generated test-cases.json (for post-verify)")
    parser.add_argument("--input", "-i", help="Path to functional specification markdown file (or merged description for post-verify)")
    parser.add_argument("--api-key", help="API key for LLM provider")
    parser.add_argument(
        "--model",
        default="openai/gpt-4o",
        help="LiteLLM model string with provider prefix (default: openai/gpt-4o)",
    )
    parser.add_argument("--output", "-o", default="output", help="Output directory (default: output)")
    parser.add_argument(
        "--resume",
        metavar="RUN_ID",
        help="Resume a previous run by id.",
    )
    parser.add_argument(
        "--max-concurrency",
        type=int,
        default=10,
        help="Max concurrent LLM calls (default: 10)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--debug-file", default="debug_log.txt", help="Debug log file path")
    parser.add_argument(
        "--type",
        nargs="+",
        choices=["positive", "negative", "edge"],
        metavar="TYPE",
        help="Test types to generate: positive, negative, edge (default: all). Example: --type positive negative",
    )

    args = parser.parse_args()

    if args.generate or args.resume:
        return _generate(args)
    if args.post_verify:
        return _post_verify(args)

    parser.print_help()
    return 1


def _validate_model_string(model: str) -> Optional[str]:
    if "/" in model:
        return None
    return (
        f"Error: --model '{model}' is missing a provider prefix. "
        f"Use LiteLLM format, e.g. openai/gpt-4o or openrouter/anthropic/claude-3.5-sonnet"
    )


def _generate(args):
    if not args.api_key:
        print("Error: --api-key is required")
        return 1

    if args.resume:
        try:
            metadata = read_sidecar(args.resume)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1
        input_path = Path(metadata.input_path)
        model = metadata.model
        output_dir = metadata.output_dir
        run_id = metadata.run_id
        resume = True
        print(f"Resuming run {run_id}")
    else:
        if not args.input:
            print("Error: --input is required")
            return 1
        model_err = _validate_model_string(args.model)
        if model_err:
            print(model_err)
            return 1
        input_path = Path(args.input)
        model = args.model
        run_id = None
        resume = False
        output_dir = None

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    if input_path.is_dir() or input_path.suffix.lower() != ".md":
        print("Error: --input must be a markdown (.md) file")
        return 1

    functional_desc = _load_from_markdown_file(md_path=input_path)

    if not resume:
        if args.output != "output":
            output_dir = args.output
        else:
            project_slug = functional_desc.get("project_name", "output").replace(" ", "_")
            model_slug = model.replace("/", "-")
            output_dir = str(Path("outputs") / "test_case_generation" / project_slug / model_slug)

        run_id = make_run_id(functional_desc.get("project_name", "run"))
        sidecar = write_sidecar(make_run_metadata(
            run_id=run_id,
            input_path=str(input_path),
            model=model,
            output_dir=output_dir,
        ))
        print(f"run_id: {run_id}")
        print(f"  Sidecar: {sidecar}")
        print(f"  Output directory: {output_dir}")
        print(f"  (use `--resume {run_id}` to continue if interrupted)")

    set_max_concurrency(args.max_concurrency)

    generator = UIASTGenerator(
        api_key=args.api_key,
        model=model,
        debug=args.debug,
        debug_file=args.debug_file,
        run_id=run_id,
    )

    test_types = set(args.type) if args.type else {"positive", "negative", "edge"}

    try:
        output = asyncio.run(generator.generate(
            functional_desc,
            output_dir=output_dir,
            resume=resume,
            test_types=test_types,
        ))
    finally:
        generator.close()

    if output:
        n_modules = len(output.get("modules", []))
        print(f"\nDone! Generated for {n_modules} module(s).")
        print(f"  Structural Model:     {output_dir}/structural-model.json")
        print(f"  Critique:   {output_dir}/structural-model-critique.json")
        print(f"  Tests:      {output_dir}/test-cases.json")
    return 0

def _post_verify(args):
    if not args.api_key:
        print("Error: --api-key is required")
        return 1
    if not args.input:
        print("Error: --input (description markdown) is required")
        return 1
    if not args.test_cases:
        print("Error: --test-cases (json file) is required")
        return 1

    input_path = Path(args.input)
    tc_path = Path(args.test_cases)
    
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    if not tc_path.exists():
        print(f"Error: Test cases file not found: {tc_path}")
        return 1

    import json
    
    try:
        with open(tc_path, "r", encoding="utf-8") as f:
            test_cases_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid test-cases JSON: {e}")
        return 1

    description_text = input_path.read_text(encoding="utf-8")
    
    # test_cases_data might be a list of modules, or a dict with "modules".
    # Assuming it's the final output of test-cases.json:
    # { "modules": [ { "test_cases": [ ... ] } ] }
    all_test_cases = []
    if isinstance(test_cases_data, dict) and "modules" in test_cases_data:
        for mod in test_cases_data["modules"]:
            all_test_cases.extend(mod.get("test_cases", []))
    elif isinstance(test_cases_data, list):
        all_test_cases = test_cases_data
    else:
        print("Error: Unknown test-cases JSON structure")
        return 1
        
    if not all_test_cases:
        print("No test cases found to process.")
        return 0

    set_max_concurrency(args.max_concurrency)
    
    generator = PostVerificationGenerator(
        api_key=args.api_key,
        model=args.model,
        debug=args.debug,
        debug_file=args.debug_file
    )
    
    asyncio.run(generator.generate(
        merged_description=description_text,
        test_cases=all_test_cases,
        output_dir=args.output
    ))
    return 0


def _parse_markdown(text: str) -> tuple:
    modules = []
    navigation_overview = ""
    module_id = 0
    current_module = None
    collecting_nav = False

    for line in text.split('\n'):
        if line.startswith('## '):
            if current_module:
                modules.append(current_module)
                current_module = None
            if collecting_nav:
                collecting_nav = False

            title = line[3:].strip()
            if title.lower().startswith('navigation'):
                collecting_nav = True
            else:
                module_id += 1
                current_module = {"id": module_id, "title": title, "description": ""}
        elif collecting_nav:
            navigation_overview += line + "\n"
        elif current_module:
            current_module["description"] += line + "\n"

    if current_module:
        modules.append(current_module)

    return navigation_overview.strip(), modules


def _load_from_markdown_file(md_path: Path) -> dict:
    spec_text = md_path.read_text(encoding='utf-8')
    navigation_overview, modules = _parse_markdown(spec_text)
    project_name = md_path.stem.replace('-', ' ').replace('_', ' ').title()
    return {
        "project_name": project_name,
        "navigation_overview": navigation_overview,
        "modules": modules,
    }


if __name__ == "__main__":
    sys.exit(main() or 0)
