#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoSpecTest Experiment Runner
==============================
Runs all combinations of:
  - 6 specs   : SwagLab, Mifos, Parabank, PHPTravels, MoodleTeacher, MoodleStudent
  - 2 models  : gpt-4o-mini, gpt-5-mini
  - 3 approaches: zero_shot, few_shot, agent
= 36 total runs

Results folder layout:
  results/
    {website}/
      {model}/
        zero_shot/   <- test-cases.json, raw_response.txt, prompt_used.txt
        few_shot/    <- test-cases.json, raw_response.txt, prompt_used.txt
        agent/       <- test-cases.json, ui-ast.json, workflows.json, ...

Usage (PowerShell):
  $env:OPENAI_API_KEY = "sk-..."
  python run_experiments.py                          # run everything
  python run_experiments.py --dry-run               # preview without calling LLMs
  python run_experiments.py --approaches zero_shot  # only zero-shot
  python run_experiments.py --specs SwagLab Mifos   # only those specs
  python run_experiments.py --summary-only          # just rebuild the summary CSV/MD
"""

import argparse
import asyncio
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# -- Load .env file if present ----------------------------------------------
def _load_dotenv():
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())

_load_dotenv()

# -- litellm (needed for zero/few-shot LLM calls) ----------------------------
try:
    import litellm
    litellm.drop_params = True          # silently drop unsupported params (temp on o-series)
    litellm.suppress_debug_info = True
    LITELLM_AVAILABLE = True
except ImportError:
    LITELLM_AVAILABLE = False

# =============================================================================
# Configuration
# =============================================================================

# model_key (folder name)  ->  {model, api_key_env, rpm}
MODELS = {
    "gpt-4o-mini": {
        "model":       "openai/gpt-4o-mini",
        "api_key_env": "OPENAI_API_KEY",
        "rpm":         500,
    },
    "gpt-5-mini": {
        "model":       "openai/gpt-5-mini",
        "api_key_env": "OPENAI_API_KEY",
        "rpm":         500,
    },
}

# Per-model asyncio semaphores to respect rate limits.
# Concurrency = rpm // 3  (assumes ~2s avg response time).
_semaphores: dict = {}

def get_semaphore(model_key: str) -> asyncio.Semaphore:
    if model_key not in _semaphores:
        rpm = MODELS[model_key]["rpm"]
        concurrency = max(1, rpm // 3)
        _semaphores[model_key] = asyncio.Semaphore(concurrency)
    return _semaphores[model_key]

# spec_key (folder name)  ->  paths
SPECS = {
    "SwagLab": {
        "spec":            "dataset/raw_specifications/SwagLab/SwagLab.md",
        "few_shot_prompt": "baselines/few_shot/SwagLab_few_shot.md",
        # If an agent run already exists in outputs/, copy it instead of re-running.
        # Set to None if no existing run.
        "existing_agent": {
            "gpt-5-mini":  None,   # no existing run
            "gpt-4o-mini": None,
        },
    },
    "Mifos": {
        "spec":            "dataset/raw_specifications/Mifos/Mifos.md",
        "few_shot_prompt": "baselines/few_shot/Mifos_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/autospectest/Mifos/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "Parabank": {
        "spec":            "dataset/raw_specifications/Parabank/Parabank.md",
        "few_shot_prompt": "baselines/few_shot/Parabank_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/autospectest/Parabank/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "PHPTravels": {
        "spec":            "dataset/raw_specifications/PHPTravels/PHPTravels.md",
        "few_shot_prompt": "baselines/few_shot/PHPTravels_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/autospectest/Phptravels/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "MoodleTeacher": {
        "spec":            "dataset/raw_specifications/Moodle/MoodleTeacher.md",
        "few_shot_prompt": "baselines/few_shot/MoodleTeacher_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/autospectest/Moodleteacher/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
    "MoodleStudent": {
        "spec":            "dataset/raw_specifications/Moodle/MoodleStudent.md",
        "few_shot_prompt": "baselines/few_shot/MoodleStudent_few_shot.md",
        "existing_agent": {
            "gpt-5-mini":  "outputs/autospectest/Moodlestudent/openai-gpt-5-mini",
            "gpt-4o-mini": None,
        },
    },
}

ZERO_SHOT_PROMPT_PATH = "baselines/zero_shot/prompt.md"
RESULTS_DIR = Path("results")

# =============================================================================
# Counters & logging
# =============================================================================

_counts = {"done": 0, "skip": 0, "error": 0}


def log(msg: str, level: str = "INFO"):
    ts = datetime.now().strftime("%H:%M:%S")
    prefix = {
        "INFO": "      ",
        "OK":   "[OK]  ",
        "SKIP": "[SKIP]",
        "ERR":  "[ERR] ",
        "HEAD": "---   ",
    }.get(level, "      ")
    print(f"[{ts}] {prefix} {msg}", flush=True)

# =============================================================================
# File helpers
# =============================================================================

def load_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def save_json(data: dict, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_text(text: str, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def extract_json(raw: str) -> dict:
    """Parse JSON from LLM response, stripping markdown fences if needed."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    m = re.search(r"```(?:json)?\s*([\s\S]+?)```", raw)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except json.JSONDecodeError:
            pass
    return {"parse_error": True, "raw_response": raw}


def out_dir(website: str, model_key: str, approach: str) -> Path:
    return RESULTS_DIR / website / model_key / approach


def compute_summary(test_cases: list) -> dict:
    s = {"total": len(test_cases),
         "positive": 0, "negative": 0, "edge": 0,
         "high_priority": 0, "medium_priority": 0, "low_priority": 0}
    for tc in test_cases:
        cat = tc.get("category", "").lower()
        if cat in s:
            s[cat] += 1
        pri = f"{tc.get('priority', '').lower()}_priority"
        if pri in s:
            s[pri] += 1
    return s

# =============================================================================
# Module parsing  (same logic as cli.py _parse_markdown)
# =============================================================================

def parse_modules(spec_path: str) -> list:
    """
    Parse a spec markdown file into a list of module dicts.
    Each ## heading (except Navigation) becomes one module.
    Returns: [{"title": str, "description": str}, ...]
    """
    text = Path(spec_path).read_text(encoding="utf-8")
    modules = []
    current = None
    collecting_nav = False

    for line in text.split("\n"):
        if line.startswith("## "):
            if current:
                modules.append(current)
                current = None
            collecting_nav = False
            title = line[3:].strip()
            if title.lower().startswith("navigation"):
                collecting_nav = True
            else:
                current = {"title": title, "description": ""}
        elif current:
            current["description"] += line + "\n"
        # navigation lines are skipped

    if current:
        modules.append(current)

    return modules


# =============================================================================
# Zero-shot / Few-shot  (per-module: one LLM call per ## section)
# =============================================================================

def build_module_prompt(approach: str, module_title: str, module_desc: str,
                        spec_info: dict, zero_shot_template: str) -> str:
    """Build the prompt for a single module."""
    template = zero_shot_template if approach == "zero_shot" \
        else load_text(spec_info["few_shot_prompt"])
    prompt = template.replace("{Module name}", module_title)
    prompt = prompt.replace("{Functional description text}", module_desc.strip())
    return prompt


async def call_llm_for_module(module_title: str, prompt: str,
                              model_str: str, api_key: str,
                              semaphore: asyncio.Semaphore = None) -> tuple:
    """Single async LLM call for one module, rate-limited by semaphore."""
    async with (semaphore or asyncio.Semaphore(999)):
        response = await litellm.acompletion(
            model=model_str,
            messages=[{"role": "user", "content": prompt}],
            api_key=api_key,
            temperature=0,
            num_retries=5,
        )
    raw = response.choices[0].message.content
    return raw, extract_json(raw)


async def run_baseline(approach: str, website: str, model_key: str,
                       model_str: str, api_key: str, spec_info: dict,
                       zero_shot_template: str, dry_run: bool,
                       folder_name: str = None):
    """
    Run zero-shot or few-shot baseline.
    Calls the LLM once per module (## section) and merges all results.
    folder_name: the actual results subfolder name (defaults to approach)
    """
    folder = folder_name or approach
    dest = out_dir(website, model_key, folder)
    result_file = dest / "test-cases.json"


    if result_file.exists():
        log(f"{website}/{model_key}/{folder} - already exists", "SKIP")
        _counts["skip"] += 1
        return

    modules = parse_modules(spec_info["spec"])
    if not modules:
        log(f"No modules found in spec: {spec_info['spec']}", "ERR")
        _counts["error"] += 1
        return

    if dry_run:
        log(f"[DRY-RUN] would call {len(modules)} modules: {website}/{model_key}/{folder}")
        return

    log(f"Starting {website}/{model_key}/{folder} ({len(modules)} modules) ...")

    dest.mkdir(parents=True, exist_ok=True)

    # Build all prompts up front
    prompts = [
        (m["title"], build_module_prompt(
            approach, m["title"], m["description"], spec_info, zero_shot_template))
        for m in modules
    ]

    # Save prompts for reproducibility
    prompts_log = "\n\n" + "="*60 + "\n\n"
    prompts_log = prompts_log.join(
        f"MODULE: {title}\n{prompt}" for title, prompt in prompts)
    save_text(prompts_log, dest / "prompts_used.txt")

    # Call LLM for all modules concurrently (rate-limited by semaphore)
    sem = get_semaphore(model_key)

    async def _call(title, prompt):
        try:
            raw, parsed = await call_llm_for_module(
                title, prompt, model_str, api_key, semaphore=sem)
            return title, raw, parsed, None
        except Exception as exc:
            return title, "", {"parse_error": True}, str(exc)

    results = await asyncio.gather(*[_call(t, p) for t, p in prompts])

    # Merge results into agent-compatible format
    all_modules = []
    all_raws = []
    global_tc_idx = 1
    total_pos = total_neg = total_edge = 0
    total_high = total_med = total_low = 0

    for title, raw, parsed, err in results:
        all_raws.append(f"=== MODULE: {title} ===\n{raw}")

        if err:
            log(f"  [ERR] {title}: {err}", "ERR")
            test_cases = []
        elif "test_cases" in parsed and isinstance(parsed["test_cases"], list):
            test_cases = parsed["test_cases"]
        elif "parse_error" in parsed:
            log(f"  [WARN] {title}: JSON parse failed", "ERR")
            test_cases = []
        else:
            test_cases = []

        # Renumber tc_id sequentially across all modules
        for tc in test_cases:
            tc["tc_id"] = f"TC-{global_tc_idx:03d}"
            global_tc_idx += 1
            cat = tc.get("category", "").lower()
            if cat == "positive":  total_pos += 1
            elif cat == "negative": total_neg += 1
            elif cat == "edge":    total_edge += 1
            pri = tc.get("priority", "").lower()
            if pri == "high":    total_high += 1
            elif pri == "medium": total_med  += 1
            elif pri == "low":   total_low  += 1

        mod_summary = compute_summary(test_cases)
        all_modules.append({
            "module":      title,
            "test_cases":  test_cases,
            "summary":     mod_summary,
        })
        log(f"  Module '{title}': {len(test_cases)} test cases")

    total_tcs = global_tc_idx - 1
    combined = {
        "project_name":  website,
        "generated_at":  datetime.utcnow().isoformat() + "Z",
        "model":         model_key,
        "approach":      folder,
        "modules":       all_modules,
        "total_summary": {
            "total_modules":   len(all_modules),
            "total_tests":     total_tcs,
            "positive":        total_pos,
            "negative":        total_neg,
            "edge":            total_edge,
            "high_priority":   total_high,
            "medium_priority": total_med,
            "low_priority":    total_low,
        },
    }

    save_json(combined, result_file)
    save_text("\n\n".join(all_raws), dest / "raw_responses.txt")

    log(f"Done: {website}/{model_key}/{folder} "
        f"({len(all_modules)} modules, {total_tcs} total test cases)", "OK")
    _counts["done"] += 1



# =============================================================================
# Zero-shot / Few-shot  (whole-file: one LLM call for the entire spec)
# =============================================================================

async def run_baseline_whole_file(approach: str, website: str, model_key: str,
                                   model_str: str, api_key: str, spec_info: dict,
                                   zero_shot_template: str, dry_run: bool):
    """
    Original whole-file baseline: one single LLM call for the entire spec.
    approach must be 'zero_shot' or 'few_shot'.
    """
    dest = out_dir(website, model_key, approach)
    result_file = dest / "test-cases.json"

    if result_file.exists():
        log(f"{website}/{model_key}/{approach} - already exists", "SKIP")
        _counts["skip"] += 1
        return

    if dry_run:
        log(f"[DRY-RUN] would call (whole-file): {website}/{model_key}/{approach}")
        return

    spec_content = load_text(spec_info["spec"])
    template = zero_shot_template if approach == "zero_shot" \
        else load_text(spec_info["few_shot_prompt"])
    prompt = template.replace("{Module name}", website)
    prompt = prompt.replace("{Functional description text}", spec_content)

    log(f"Calling LLM (whole-file): {website}/{model_key}/{approach} ...")
    sem = get_semaphore(model_key)
    try:
        async with sem:
            response = await litellm.acompletion(
                model=model_str,
                messages=[{"role": "user", "content": prompt}],
                api_key=api_key,
                temperature=0,
                num_retries=5,
            )
        raw = response.choices[0].message.content

        parsed = extract_json(raw)

        if "test_cases" in parsed and isinstance(parsed["test_cases"], list):
            parsed["summary"] = compute_summary(parsed["test_cases"])
        parsed.setdefault("_meta", {}).update({
            "website": website, "model": model_key,
            "approach": approach,
            "generated_at": datetime.utcnow().isoformat() + "Z",
        })

        save_json(parsed, result_file)
        save_text(raw, dest / "raw_response.txt")
        save_text(prompt, dest / "prompt_used.txt")

        n = len(parsed.get("test_cases", []))
        log(f"Done: {website}/{model_key}/{approach} ({n} test cases)", "OK")
        _counts["done"] += 1

    except Exception as exc:
        log(f"ERROR: {website}/{model_key}/{approach}: {exc}", "ERR")
        dest.mkdir(parents=True, exist_ok=True)
        save_json({"error": str(exc)}, dest / "error.json")
        _counts["error"] += 1


# =============================================================================
# Agent runner
# =============================================================================

def copy_existing_agent(src_str: str, dest: Path, website: str, model_key: str):
    """Copy a pre-existing agent output directory into results/."""
    src = Path(src_str)
    if not src.exists():
        log(f"Existing agent dir not found: {src}", "ERR")
        _counts["error"] += 1
        return False
    dest.mkdir(parents=True, exist_ok=True)
    copied = 0
    for item in src.iterdir():
        d = dest / item.name
        if item.is_file():
            shutil.copy2(item, d)
            copied += 1
        elif item.is_dir():
            if d.exists():
                shutil.rmtree(d)
            shutil.copytree(item, d)
            copied += 1
    log(f"Copied {copied} items from existing run: {website}/{model_key}/agent", "OK")
    _counts["done"] += 1
    return True


def run_agent(website: str, model_key: str, model_str: str, api_key: str,
              spec_info: dict, dry_run: bool):
    dest = out_dir(website, model_key, "agent")
    result_file = dest / "test-cases.json"

    # Already copied/run?
    if result_file.exists():
        log(f"{website}/{model_key}/agent - already exists", "SKIP")
        _counts["skip"] += 1
        return

    # Use pre-existing output from outputs/?
    existing = spec_info.get("existing_agent", {}).get(model_key)
    if existing:
        log(f"Copying existing agent output: {website}/{model_key}/agent ...")
        copy_existing_agent(existing, dest, website, model_key)
        return

    # Fresh agent run
    if dry_run:
        log(f"[DRY-RUN] would run agent: {website}/{model_key}/agent")
        return

    dest.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable, "-m", "autospectest",
        "--generate",
        "--input",   spec_info["spec"],
        "--api-key", api_key,
        "--model",   model_str,
        "--output",  str(dest),
    ]
    log(f"Running agent: {website}/{model_key}/agent ...")
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=900,
            env={**os.environ, MODELS[model_key]["api_key_env"]: api_key},
        )
        log_file = dest / "agent_run.log"
        log_file.write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8")

        if proc.returncode == 0:
            log(f"Done: {website}/{model_key}/agent", "OK")
            _counts["done"] += 1
        else:
            log(f"Agent failed (rc={proc.returncode}): {website}/{model_key}/agent", "ERR")
            _counts["error"] += 1
    except subprocess.TimeoutExpired:
        log(f"TIMEOUT (>15 min): {website}/{model_key}/agent", "ERR")
        _counts["error"] += 1
    except Exception as exc:
        log(f"ERROR: {website}/{model_key}/agent: {exc}", "ERR")
        _counts["error"] += 1

# =============================================================================
# Summary report
# =============================================================================

def write_summary():
    rows = []
    for wsite in sorted(RESULTS_DIR.iterdir()):
        if not wsite.is_dir() or wsite.name.startswith("."):
            continue
        for mdir in sorted(wsite.iterdir()):
            if not mdir.is_dir():
                continue
            for adir in sorted(mdir.iterdir()):
                if not adir.is_dir():
                    continue
                tc_file = adir / "test-cases.json"
                row = {
                    "website": wsite.name, "model": mdir.name,
                    "approach": adir.name, "status": "MISSING",
                    "total": 0, "positive": 0, "negative": 0, "edge": 0,
                    "high": 0, "medium": 0, "low": 0,
                }
                if tc_file.exists():
                    try:
                        data = json.loads(tc_file.read_text(encoding="utf-8"))
                        # Agent output has total_summary
                        if "total_summary" in data:
                            s = data["total_summary"]
                            row.update({
                                "status":   "OK",
                                "total":    s.get("total_tests", s.get("total", 0)),
                                "positive": s.get("positive", 0),
                                "negative": s.get("negative", 0),
                                "edge":     s.get("edge", 0),
                                "high":     s.get("high_priority", 0),
                                "medium":   s.get("medium_priority", 0),
                                "low":      s.get("low_priority", 0),
                            })
                        # Baseline output has summary
                        elif "summary" in data:
                            s = data["summary"]
                            row.update({
                                "status":   "PARSE_ERR" if data.get("parse_error") else "OK",
                                "total":    s.get("total", 0),
                                "positive": s.get("positive", 0),
                                "negative": s.get("negative", 0),
                                "edge":     s.get("edge", 0),
                                "high":     s.get("high_priority", 0),
                                "medium":   s.get("medium_priority", 0),
                                "low":      s.get("low_priority", 0),
                            })
                        else:
                            row["status"] = "UNKNOWN_FORMAT"
                    except Exception as e:
                        row["status"] = f"ERR:{e}"
                rows.append(row)

    if not rows:
        log("No results found to summarise.")
        return

    # CSV
    fields = ["website", "model", "approach", "status",
              "total", "positive", "negative", "edge", "high", "medium", "low"]
    csv_path = RESULTS_DIR / "experiment_summary.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    log(f"Summary CSV  -> {csv_path}")

    # Markdown
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Experiment Results Summary\n",
        f"Generated: {ts}\n",
        "| Website | Model | Approach | Status | Total | Positive | Negative | Edge | High | Medium | Low |",
        "|---------|-------|----------|--------|-------|----------|----------|------|------|--------|-----|",
    ]
    for r in rows:
        lines.append(
            f"| {r['website']} | {r['model']} | {r['approach']} | {r['status']} "
            f"| {r['total']} | {r['positive']} | {r['negative']} | {r['edge']} "
            f"| {r['high']} | {r['medium']} | {r['low']} |"
        )
    md_path = RESULTS_DIR / "experiment_summary.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"Summary MD   -> {md_path}")

# =============================================================================
# Main
# =============================================================================

async def main():
    parser = argparse.ArgumentParser(description="AutoSpecTest Experiment Runner")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview all runs without making any LLM calls")
    parser.add_argument("--approaches", nargs="+",
                        choices=["zero_shot", "few_shot",
                                 "zero_shot_per_module", "few_shot_per_module",
                                 "agent"],
                        default=["zero_shot", "few_shot",
                                 "zero_shot_per_module", "few_shot_per_module",
                                 "agent"],
                        metavar="APPROACH")
    parser.add_argument("--specs", nargs="+",
                        choices=list(SPECS.keys()),
                        default=list(SPECS.keys()),
                        metavar="SPEC")
    parser.add_argument("--models", nargs="+",
                        choices=list(MODELS.keys()),
                        default=list(MODELS.keys()),
                        metavar="MODEL")
    parser.add_argument("--summary-only", action="store_true",
                        help="Skip all runs; just regenerate the summary report")
    args = parser.parse_args()

    if args.summary_only:
        write_summary()
        return

    # Validate that at least the required API keys are present
    if not args.dry_run:
        missing = []
        for mk in args.models:
            env_var = MODELS[mk]["api_key_env"]
            if not os.environ.get(env_var):
                missing.append(f"  {mk}: needs {env_var}")
        if missing:
            print("Error: Missing API keys for the following models:")
            for m in missing:
                print(m)
            print("Add them to your .env file and re-run.")
            sys.exit(1)

    if not LITELLM_AVAILABLE and not args.dry_run:
        baseline_needed = set(args.approaches) & {"zero_shot", "few_shot"}
        if baseline_needed:
            print("Error: litellm is not installed. Run: pip install -e .")
            sys.exit(1)

    total = len(args.specs) * len(args.models) * len(args.approaches)
    print()
    log("AutoSpecTest Experiment Runner", "HEAD")
    log(f"Specs     : {', '.join(args.specs)}")
    log(f"Models    : {', '.join(args.models)}")
    log(f"Approaches: {', '.join(args.approaches)}")
    log(f"Total runs: {total}")
    log(f"Output    : {RESULTS_DIR.resolve()}")
    if args.dry_run:
        log("DRY-RUN mode — no LLM calls will be made")
    print()

    zero_shot_template = load_text(ZERO_SHOT_PROMPT_PATH)

    for website in args.specs:
        spec_info = SPECS[website]
        log(f"=== {website} ===", "HEAD")

        for model_key in args.models:
            model_cfg  = MODELS[model_key]
            model_str  = model_cfg["model"]
            api_key    = os.environ.get(model_cfg["api_key_env"], "")

            # Whole-file baselines (zero_shot / few_shot)
            whole_file_coros = [
                run_baseline_whole_file(ap, website, model_key, model_str, api_key,
                                        spec_info, zero_shot_template, args.dry_run)
                for ap in args.approaches
                if ap in ("zero_shot", "few_shot")
            ]
            if whole_file_coros:
                await asyncio.gather(*whole_file_coros)

            # Per-module baselines (zero_shot_per_module / few_shot_per_module)
            per_module_map = {
                "zero_shot_per_module": "zero_shot",
                "few_shot_per_module":  "few_shot",
            }
            per_module_coros = [
                run_baseline(per_module_map[ap], website, model_key, model_str,
                             api_key, spec_info, zero_shot_template, args.dry_run,
                             folder_name=ap)
                for ap in args.approaches
                if ap in per_module_map
            ]
            if per_module_coros:
                await asyncio.gather(*per_module_coros)

            # Agent runs sequentially (subprocess)
            if "agent" in args.approaches:
                run_agent(website, model_key, model_str, api_key,
                          spec_info, args.dry_run)

        print()

    print("=" * 60)
    log(f"All done.  OK={_counts['done']}  Skipped={_counts['skip']}  Errors={_counts['error']}")

    if not args.dry_run:
        print()
        write_summary()


if __name__ == "__main__":
    asyncio.run(main())
