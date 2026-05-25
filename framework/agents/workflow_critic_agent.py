"""Workflow Critic Agent: audits an extracted workflow list against the UI-AST and functional description."""

import json
from importlib import resources
from typing import Any, Dict, List

from autospectest.framework.agents.base import BaseAgent

_PROMPT = resources.files("autospectest.prompts").joinpath("workflow_critic.md").read_text(encoding="utf-8")


class WorkflowCriticAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Workflow-Critic"

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
