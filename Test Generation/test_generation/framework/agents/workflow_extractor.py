"""Workflow Extractor Agent: enumerates all distinct executable workflows from a Structural Model."""

import json
from importlib import resources
from typing import Any, Dict, List, Optional

from test_generation.framework.agents.base import BaseAgent

_PROMPT_TEMPLATE: str = (
    resources.files("test_generation.prompts")
    .joinpath("workflow_extractor.md")
    .read_text(encoding="utf-8")
)

# The entire ORCHESTRATOR-comment block that wraps {fixes_block} in the template.
# Replaced with the real fixes on attempt 2+, or stripped entirely on attempt 1.
_FIXES_COMMENT_BLOCK = (
    "{fixes_block}\n"
    "[ORCHESTRATOR: if attempt_number > 1, replace {fixes_block} with the following block,\n"
    "populated with the validator's fixes array. If attempt_number == 1, remove the block entirely.]\n"
    "\n"
    "--- VALIDATOR FIXES — APPLY ALL OF THESE BEFORE GENERATING ---\n"
    "{fixes}\n"
    "Every item above is a confirmed error from the previous attempt. Do not repeat them.\n"
    "--- END FIXES ---"
)


def _render_extractor_system_prompt(attempt: int, max_attempts: int, fixes: List[str]) -> str:
    """Return the extractor system prompt with all template slots filled."""
    if attempt == 1 or not fixes:
        fixes_section = ""
    else:
        bullet_lines = "\n".join(f"- {f}" for f in fixes)
        fixes_section = (
            "--- VALIDATOR FIXES — APPLY ALL OF THESE BEFORE GENERATING ---\n"
            f"{bullet_lines}\n"
            "Every item above is a confirmed error from the previous attempt. "
            "Do not repeat them.\n"
            "--- END FIXES ---"
        )

    rendered = _PROMPT_TEMPLATE.replace(_FIXES_COMMENT_BLOCK, fixes_section)
    rendered = rendered.replace("{attempt_number}", str(attempt))
    rendered = rendered.replace("{max_attempts}", str(max_attempts))
    return rendered


class WorkflowExtractorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Workflow-Extractor"

    @property
    def system_prompt(self) -> str:
        return getattr(self, "_active_system_prompt", _PROMPT_TEMPLATE)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def run(
        self,
        module_title: str,
        ast: Dict[str, Any],
        description: str,
        fixes: Optional[List[str]] = None,
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_extractor_system_prompt(
            attempt, max_attempts, fixes or []
        )
        return self.call_llm_json(
            self._build_prompt(module_title, ast, description),
            temperature=0.2,
            max_tokens=8192,
        )

    async def arun(
        self,
        module_title: str,
        ast: Dict[str, Any],
        description: str,
        fixes: Optional[List[str]] = None,
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_extractor_system_prompt(
            attempt, max_attempts, fixes or []
        )
        return await self.acall_llm_json(
            self._build_prompt(module_title, ast, description),
            temperature=0.2,
            max_tokens=8192,
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_prompt(module_title: str, ast: Dict[str, Any], description: str) -> str:
        return (
            f"<module_name>{module_title}</module_name>\n\n"
            f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>\n\n"
            f"<description>\n{description}\n</description>"
        )

    @staticmethod
    def format_workflows_block(workflows: Optional[List[Dict[str, Any]]]) -> str:
        """Render the compact <workflows> block appended to Stage 2 agent prompts."""
        if not workflows:
            return ""
        lines = ["<workflows>"]
        for wf in workflows:
            branch = wf.get("conditional_branch") or "none"
            lines.append(
                f"{wf['wf_id']} | {wf['name']} | actor: {wf.get('actor', '<role>')} "
                f"| branch: {branch} | terminal: {wf.get('terminal_action', '')} "
                f"| on_success: {wf.get('on_success', '')}"
            )
        lines.append("</workflows>")
        return "\n".join(lines)
