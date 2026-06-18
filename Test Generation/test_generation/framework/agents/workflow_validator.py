"""Workflow Critic Agent: audits an extracted workflow list against the Structural Model and functional description."""

import json
from importlib import resources
from typing import Any, Dict, List

from test_generation.framework.agents.base import BaseAgent

_PROMPT = resources.files("test_generation.prompts").joinpath("workflow_validator.md").read_text(encoding="utf-8")


class WorkflowValidatorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Workflow-Validator"

    @property
    def system_prompt(self) -> str:
        return _PROMPT

    def run(self, description: str, ast: Dict[str, Any], workflows: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self.call_llm_json(
            self._build_prompt(description, ast, workflows),
            temperature=0.1,
            max_tokens=4096,
            reasoning_effort="medium",
        )

    async def arun(self, description: str, ast: Dict[str, Any], workflows: List[Dict[str, Any]]) -> Dict[str, Any]:
        return await self.acall_llm_json(
            self._build_prompt(description, ast, workflows),
            temperature=0.1,
            max_tokens=4096,
            reasoning_effort="medium",
        )

    @staticmethod
    def _build_prompt(description: str, ast: Dict[str, Any], workflows: List[Dict[str, Any]]) -> str:
        return (
            f"<description>\n{description}\n</description>\n\n"
            f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>\n\n"
            f"<workflows>\n{json.dumps(workflows, indent=2)}\n</workflows>"
        )
