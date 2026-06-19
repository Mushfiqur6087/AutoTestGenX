"""Shared utilities for test case generator agents."""

import json
from typing import Any, Dict, List, Optional

from test_generation.framework.agents.workflow_extractor import WorkflowExtractorAgent


def build_test_prompt(
    module_title: str,
    ast: Dict[str, Any],
    description: str,
    workflows: Optional[List[Dict[str, Any]]] = None,
) -> str:
    """Build the standard user prompt for all three test case generators.

    Assembles the <module_name>, <ast>, <description>, and <workflows> blocks
    that every Stage 3 agent receives as its user message.
    """
    prompt = (
        f"<module_name>{module_title}</module_name>\n\n"
        f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>\n\n"
        f"<description>\n{description}\n</description>"
    )
    wf_block = WorkflowExtractorAgent.format_workflows_block(workflows)
    if wf_block:
        prompt += f"\n\n{wf_block}"
    return prompt
