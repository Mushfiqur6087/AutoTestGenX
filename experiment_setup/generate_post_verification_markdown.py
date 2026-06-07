import json
import os
from pathlib import Path
from typing import Dict, Any, List

def format_steps(steps: List[str]) -> str:
    if not steps:
        return "*No steps provided.*"
    return "\n".join(f"{i+1}. {step}" for i, step in enumerate(steps))

def generate_markdown(post_verifications: List[Dict[str, Any]], test_cases_map: Dict[str, Dict[str, Any]]) -> str:
    md_lines = ["# Post-Verification Specifications\n"]
    
    for pv in post_verifications:
        tc_id = pv.get("test_case_id")
        v_type = pv.get("verification_type", "unknown")
        coverage = pv.get("coverage", "verifiable")
        body = pv.get("body", {})
        
        tc_data = test_cases_map.get(tc_id, {})
        title = tc_data.get("test_case", tc_data.get("title", "Unknown Title"))
        description = tc_data.get("description", "")
        category = tc_data.get("category", "positive")
        steps = tc_data.get("steps", [])
        expected_result = tc_data.get("expected_result", "")
        
        md_lines.append(f"### [{tc_id}] {title}")
        md_lines.append(f"**Category**: `{category}` | **Verification Type**: `{v_type}` | **Coverage**: `{coverage}`\n")
        
        if coverage == "partial" and pv.get("coverage_note"):
            md_lines.append(f"**Coverage Note**: *{pv.get('coverage_note')}*\n")
            
        if description:
            md_lines.append("**Original Test Case Description:**")
            md_lines.append(f"> {description}\n")
        
        md_lines.append("**Original Steps:**")
        md_lines.append(f"{format_steps(steps)}\n")
        
        if expected_result:
            md_lines.append(f"**Original Expected Result:** {expected_result}\n")
        
        md_lines.append("---\n")
        md_lines.append("#### Verification Plan\n")
        
        if v_type == "cross_actor":
            actor_a = body.get("actor_a", {})
            actor_b = body.get("actor_b", {})
            
            if actor_a:
                md_lines.append(f"**Actor A (Role: `{actor_a.get('role', 'unknown')}`)**")
                if "session" in actor_a:
                    md_lines.append(f"- **Session**: `{actor_a.get('session')}`")
                if "navigate_to" in actor_a:
                    md_lines.append(f"- **Navigate To**: `{actor_a.get('navigate_to')}`")
                md_lines.append(f"- **Action**: {actor_a.get('action', '')}\n")
                
            if actor_b:
                md_lines.append(f"**Actor B (Role: `{actor_b.get('role', 'unknown')}`)**")
                if "session" in actor_b:
                    md_lines.append(f"- **Session**: `{actor_b.get('session')}`")
                if "navigate_to" in actor_b:
                    md_lines.append(f"- **Navigate To**: `{actor_b.get('navigate_to')}`")
                md_lines.append(f"- **Action**: {actor_b.get('action', '')}")
                if "observe" in actor_b:
                    md_lines.append("- **Observe**:")
                    for obs in actor_b.get("observe", []):
                        md_lines.append(f"  - {obs}")
                md_lines.append("")
                if "expected_change" in actor_b:
                    md_lines.append(f"**Expected Change**: {actor_b.get('expected_change')}\n")
                    
        else:
            pre_check = body.get("pre_check", {})
            post_check = body.get("post_check", {})
            
            if pre_check:
                md_lines.append("**Pre-Check**")
                if "navigate_to" in pre_check:
                    md_lines.append(f"- **Navigate To**: `{pre_check.get('navigate_to')}`")
                if "observe" in pre_check:
                    md_lines.append("- **Observe**:")
                    for obs in pre_check.get("observe", []):
                        md_lines.append(f"  - {obs}")
                md_lines.append("")
                
            if post_check:
                md_lines.append("**Post-Check**")
                if "navigate_to" in post_check:
                    md_lines.append(f"- **Navigate To**: `{post_check.get('navigate_to')}`")
                if "observe" in post_check:
                    md_lines.append("- **Observe**:")
                    for obs in post_check.get("observe", []):
                        md_lines.append(f"  - {obs}")
                md_lines.append("")
                if "expected_change" in post_check:
                    md_lines.append(f"**Expected Change**: {post_check.get('expected_change')}\n")
                    
        md_lines.append("---\n")
        
    return "\n".join(md_lines)

def process_results_directory(base_dir: str):
    root = Path(base_dir)
    for pv_file in root.rglob("post-verifications.json"):
        agent_dir = pv_file.parent
        tc_file = agent_dir / "test-cases.json"
        
        if not tc_file.exists():
            print(f"Skipping {agent_dir}: No test-cases.json found.")
            continue
            
        print(f"Processing {agent_dir}...")
        
        # Load post verifications
        with open(pv_file, "r", encoding="utf-8") as f:
            try:
                post_verifications = json.load(f)
            except json.JSONDecodeError:
                print(f"Error parsing JSON in {pv_file}")
                continue
                
        # Load test cases
        with open(tc_file, "r", encoding="utf-8") as f:
            try:
                tc_data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error parsing JSON in {tc_file}")
                continue
                
        # Flatten test cases into a map by tc_id
        tc_map = {}
        if isinstance(tc_data, dict) and "modules" in tc_data:
            for mod in tc_data.get("modules", []):
                for tc in mod.get("test_cases", []):
                    if "tc_id" in tc:
                        tc_map[tc["tc_id"]] = tc
        elif isinstance(tc_data, list):
            for tc in tc_data:
                if "tc_id" in tc:
                    tc_map[tc["tc_id"]] = tc
                    
        # Generate markdown
        md_content = generate_markdown(post_verifications, tc_map)
        
        # Save markdown
        out_file = agent_dir / "post-verifications.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"Saved {out_file}")

if __name__ == "__main__":
    results_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
    process_results_directory(results_dir)
