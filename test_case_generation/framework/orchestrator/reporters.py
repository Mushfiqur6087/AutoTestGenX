from typing import Dict, List, Any

def _md_escape(text: str) -> str:
    """Escape pipe characters and collapse newlines for markdown table cells."""
    if not isinstance(text, str):
        text = str(text)
    return text.replace("|", "\\|").replace("\n", " ")


def _render_critique_md(data: dict) -> str:
    lines = []
    lines.append(f"# Semantic Critique — {data.get('project_name', '')}")
    lines.append("")
    lines.append(f"Generated: {data.get('generated_at', '')}")
    lines.append("")

    for module in data.get("modules", []):
        title = module.get("module_title", "Unknown")
        lines.append(f"## {title}")
        lines.append("")

        error = module.get("error")
        if error:
            lines.append(f"> **Error:** {error}")
            lines.append("")
            continue

        critique = module.get("critique") or {}
        forced = module.get("forced_ship", False)

        verdict = critique.get("verdict", "—")
        verdict_label = "yes" if verdict == "yes" else "retry (forced ship)" if forced else "retry"
        lines.append(f"**Verdict:** {verdict_label}  ")
        lines.append(f"**Forced ship:** {'yes' if forced else 'no'}  ")
        lines.append("")

        summary = critique.get("summary", "")
        if summary:
            lines.append(f"{summary}")
            lines.append("")

        missing = critique.get("missing", [])
        if missing:
            lines.append("**Missing:**")
            lines.append("")
            for item in missing:
                lines.append(f"- {item}")
            lines.append("")
        else:
            lines.append("**Missing:** none")
            lines.append("")

        phantoms = critique.get("phantoms", [])
        if phantoms:
            lines.append("**Phantoms (hallucinations):**")
            lines.append("")
            for item in phantoms:
                lines.append(f"- {item}")
            lines.append("")
        else:
            lines.append("**Phantoms:** none")
            lines.append("")

        fixes = critique.get("fixes", [])
        if fixes:
            lines.append("**Fixes applied:**")
            lines.append("")
            for fix in fixes:
                lines.append(f"- {fix}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def _render_workflow_critique_md(data: dict) -> str:
    lines = []
    lines.append(f"# Workflow Critique — {data.get('project_name', '')}")
    lines.append("")
    lines.append(f"Generated: {data.get('generated_at', '')}")
    lines.append("")

    for module in data.get("modules", []):
        title = module.get("module_title", "Unknown")
        lines.append(f"## {title}")
        lines.append("")

        error = module.get("error")
        if error:
            lines.append(f"> **Error:** {error}")
            lines.append("")
            continue

        critique = module.get("critique") or {}
        forced = module.get("forced_ship", False)

        verdict = critique.get("verdict", "—")
        verdict_label = "yes" if verdict == "yes" else "retry (forced ship)" if forced else "retry"
        lines.append(f"**Verdict:** {verdict_label}  ")
        lines.append(f"**Forced ship:** {'yes' if forced else 'no'}  ")
        lines.append("")

        summary = critique.get("summary", "")
        if summary:
            lines.append(f"{summary}")
            lines.append("")

        missing = critique.get("missing", [])
        if missing:
            lines.append("**Missing workflows:**")
            lines.append("")
            for item in missing:
                lines.append(f"- {item}")
            lines.append("")
        else:
            lines.append("**Missing workflows:** none")
            lines.append("")

        phantoms = critique.get("phantoms", [])
        if phantoms:
            lines.append("**Phantom workflows:**")
            lines.append("")
            for item in phantoms:
                lines.append(f"- {item}")
            lines.append("")
        else:
            lines.append("**Phantom workflows:** none")
            lines.append("")

        fixes = critique.get("fixes", [])
        if fixes:
            lines.append("**Fixes applied:**")
            lines.append("")
            for fix in fixes:
                lines.append(f"- {fix}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def _render_test_cases_md(data: dict) -> str:
    lines = []
    lines.append(f"# Test Cases — {data.get('project_name', '')}")
    lines.append("")
    lines.append(f"Generated: {data.get('generated_at', '')}  ")
    lines.append(f"Model: {data.get('model', '')}  ")
    lines.append("")

    total = data.get("total_summary", {})
    if total:
        lines.append("## Summary")
        lines.append("")
        lines.append("| Modules | Total | Positive | Negative | Edge | High | Medium | Low |")
        lines.append("|---------|-------|----------|----------|------|------|--------|-----|")
        lines.append(
            f"| {total.get('total_modules', 0)}"
            f" | {total.get('total_tests', 0)}"
            f" | {total.get('positive', 0)}"
            f" | {total.get('negative', 0)}"
            f" | {total.get('edge', 0)}"
            f" | {total.get('high_priority', 0)}"
            f" | {total.get('medium_priority', 0)}"
            f" | {total.get('low_priority', 0)} |"
        )
        lines.append("")

    _CATEGORY_ORDER = [("positive", "Positive Tests"), ("negative", "Negative Tests"), ("edge", "Edge & Boundary Tests")]

    for module in data.get("modules", []):
        module_name = module.get("module", "Unknown")
        lines.append(f"## {module_name}")
        lines.append("")

        error = module.get("error")
        if error:
            lines.append(f"> **Error:** {error}")
            lines.append("")
            continue

        summary = module.get("summary", {})
        if summary:
            lines.append(
                f"Total: **{summary.get('total', 0)}** "
                f"(positive: {summary.get('positive', 0)}, "
                f"negative: {summary.get('negative', 0)}, "
                f"edge: {summary.get('edge', 0)})"
            )
            lines.append("")

        all_cases = module.get("test_cases", [])
        by_category: Dict[str, List] = {"positive": [], "negative": [], "edge": []}
        for tc in all_cases:
            cat = tc.get("category", "edge")
            by_category.setdefault(cat, []).append(tc)

        for cat_key, cat_label in _CATEGORY_ORDER:
            cases = by_category.get(cat_key, [])
            if not cases:
                continue

            lines.append(f"### {cat_label}")
            lines.append("")
            lines.append("| TC ID | WF Ref | Test Case | Preconditions | Steps | Expected Result | Priority |")
            lines.append("|-------|--------|-----------|---------------|-------|-----------------|----------|")

            for tc in cases:
                tc_id = tc.get("tc_id", "")
                wf_ref = tc.get("wf_ref") or ""
                name = _md_escape(tc.get("test_case", ""))
                preconds = tc.get("preconditions", [])
                preconds_str = _md_escape(", ".join(preconds) if isinstance(preconds, list) else str(preconds))
                steps = tc.get("steps", [])
                if isinstance(steps, list):
                    steps_str = "<br>".join(
                        s if (s[:2].rstrip(".").isdigit()) else f"{i}. {s}"
                        for i, s in enumerate(steps, 1)
                    )
                else:
                    steps_str = _md_escape(str(steps))
                expected = _md_escape(tc.get("expected_result", ""))
                priority = tc.get("priority", "")
                subcategory = tc.get("subcategory", "")
                tc_id_cell = f"{tc_id} ({subcategory})" if subcategory else tc_id

                lines.append(f"| {tc_id_cell} | {wf_ref} | {name} | {preconds_str} | {steps_str} | {expected} | {priority} |")

            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)
