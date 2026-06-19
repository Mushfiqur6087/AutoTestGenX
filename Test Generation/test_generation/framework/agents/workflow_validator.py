"""Workflow Validator Agent: audits an extracted workflow list against the Structural Model and functional description."""

import json
from importlib import resources
from typing import Any, Dict, List

from test_generation.framework.agents.base import BaseAgent

_PROMPT_TEMPLATE: str = (
    resources.files("test_generation.prompts")
    .joinpath("workflow_validator.md")
    .read_text(encoding="utf-8")
)

# The entire ORCHESTRATOR-comment block that wraps {final_attempt_warning} in the template.
_FINAL_WARNING_COMMENT_BLOCK = (
    "{final_attempt_warning}\n"
    "[ORCHESTRATOR: if attempt_number == max_attempts, replace {final_attempt_warning} with:\n"
    "\"WARNING — This is the final allowed attempt. If critical errors remain, still return\n"
    "retry — the orchestrator will escalate rather than regenerate again.\"\n"
    "Otherwise remove it.]"
)

_FINAL_WARNING_TEXT = (
    "WARNING — This is the final allowed attempt. If critical errors remain, still return\n"
    "retry — the orchestrator will escalate rather than regenerate again."
)


def _render_validator_system_prompt(attempt: int, max_attempts: int) -> str:
    """Return the workflow validator system prompt with all template slots filled."""
    warning = _FINAL_WARNING_TEXT if attempt == max_attempts else ""
    rendered = _PROMPT_TEMPLATE.replace(_FINAL_WARNING_COMMENT_BLOCK, warning)
    rendered = rendered.replace("{attempt_number}", str(attempt))
    rendered = rendered.replace("{max_attempts}", str(max_attempts))
    return rendered


class WorkflowValidatorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Workflow-Validator"

    @property
    def system_prompt(self) -> str:
        return getattr(self, "_active_system_prompt", _PROMPT_TEMPLATE)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def run(
        self,
        description: str,
        ast: Dict[str, Any],
        workflows: List[Dict[str, Any]],
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_validator_system_prompt(attempt, max_attempts)
        return self.call_llm_json(
            self._build_prompt(description, ast, workflows),
            temperature=0.1,
            max_tokens=4096,
            reasoning_effort="medium",
        )

    async def arun(
        self,
        description: str,
        ast: Dict[str, Any],
        workflows: List[Dict[str, Any]],
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_validator_system_prompt(attempt, max_attempts)
        return await self.acall_llm_json(
            self._build_prompt(description, ast, workflows),
            temperature=0.1,
            max_tokens=4096,
            reasoning_effort="medium",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_prompt(description: str, ast: Dict[str, Any], workflows: List[Dict[str, Any]]) -> str:
        return (
            f"<description>\n{description}\n</description>\n\n"
            f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>\n\n"
            f"<workflows>\n{json.dumps(workflows, indent=2)}\n</workflows>"
        )
