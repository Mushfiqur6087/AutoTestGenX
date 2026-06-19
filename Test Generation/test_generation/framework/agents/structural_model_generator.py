"""Structural Model Agent: converts a module's functional description into a UI Abstract Syntax Tree."""

from importlib import resources
from typing import Any, Dict, List, Optional

from test_generation.framework.agents.base import BaseAgent

_PROMPT_TEMPLATE: str = (
    resources.files("test_generation.prompts")
    .joinpath("structural_model_generator.md")
    .read_text(encoding="utf-8")
)

# The entire ORCHESTRATOR-comment block that wraps {fixes_block} in the template.
# This literal text is replaced at render time — either with the real fixes block
# (attempt > 1) or with an empty string (attempt == 1).
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


def _render_generator_system_prompt(attempt: int, max_attempts: int, fixes: List[str]) -> str:
    """Return the generator system prompt with all template slots filled."""
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


class StructuralModelGeneratorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Structural Model Agent"

    @property
    def system_prompt(self) -> str:
        # Returns a pre-rendered prompt if one has been set for the current call;
        # falls back to the raw template so the agent can still be instantiated
        # without calling arun first (e.g., in tests).
        return getattr(self, "_active_system_prompt", _PROMPT_TEMPLATE)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def run(
        self,
        module: Dict[str, Any],
        fixes: Optional[List[str]] = None,
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_generator_system_prompt(
            attempt, max_attempts, fixes or []
        )
        return self.call_llm_json(
            self._build_prompt(module),
            temperature=0.1,
            max_tokens=8192,
            reasoning_effort="medium",
        )

    async def arun(
        self,
        module: Dict[str, Any],
        fixes: Optional[List[str]] = None,
        attempt: int = 1,
        max_attempts: int = 3,
    ) -> Dict[str, Any]:
        self._active_system_prompt = _render_generator_system_prompt(
            attempt, max_attempts, fixes or []
        )
        return await self.acall_llm_json(
            self._build_prompt(module),
            temperature=0.1,
            max_tokens=8192,
            reasoning_effort="medium",
        )

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_prompt(module: Dict[str, Any]) -> str:
        return f"Module: {module['title']}\n\n{module['description']}"
