"""Structural Model Validator Agent: audits Structural Model JSON against the source functional description."""

import json
from importlib import resources
from typing import Any, Dict

from test_generation.framework.agents.base import BaseAgent

_PROMPT_TEMPLATE: str = (
    resources.files("test_generation.prompts")
    .joinpath("structural_model_validator.md")
    .read_text(encoding="utf-8")
)

# The entire ORCHESTRATOR-comment block that wraps {final_attempt_warning} in the template.
# Replaced with the actual warning text on the final attempt, or with "" otherwise.
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
    """Return the validator system prompt with all template slots filled."""
    warning = _FINAL_WARNING_TEXT if attempt == max_attempts else ""
    rendered = _PROMPT_TEMPLATE.replace(_FINAL_WARNING_COMMENT_BLOCK, warning)
    rendered = rendered.replace("{attempt_number}", str(attempt))
    rendered = rendered.replace("{max_attempts}", str(max_attempts))
    return rendered


class StructuralModelValidatorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Structural Model Validator"

    @property
    def system_prompt(self) -> str:
        # Returns the pre-rendered prompt set for the current call, or the raw
        # template as a safe fallback (e.g., during tests / direct instantiation).
        return getattr(self, "_active_system_prompt", _PROMPT_TEMPLATE)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def run(
        self,
        description: str,
        ast: Dict[str, Any],
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_validator_system_prompt(attempt, max_attempts)
        return self.call_llm_json(
            self._build_prompt(description, ast),
            temperature=0.1,
            max_tokens=6144,
            reasoning_effort="medium",
        )

    async def arun(
        self,
        description: str,
        ast: Dict[str, Any],
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_validator_system_prompt(attempt, max_attempts)
        return await self.acall_llm_json(
            self._build_prompt(description, ast),
            temperature=0.1,
            max_tokens=6144,
            reasoning_effort="medium",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_prompt(description: str, ast: Dict[str, Any]) -> str:
        return (
            f"<description>\n{description}\n</description>\n\n"
            f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>"
        )
