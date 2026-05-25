"""Workflow Extractor Agent: enumerates all distinct executable workflows from a UI-AST."""

import json
from importlib import resources
from typing import Any, Dict, List, Optional

from autospectest.framework.agents.base import BaseAgent

_PROMPT = resources.files("autospectest.prompts").joinpath("workflow_extractor.md").read_text(encoding="utf-8")


class WorkflowExtractorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Workflow-Extractor"

    @property
    def system_prompt(self) -> str:
        return _PROMPT

    def run(
        self,
        module_title: str,
        ast: Dict[str, Any],
        description: str,
        fixes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return self.call_llm_json(
            self._build_prompt(module_title, ast, description, fixes),
            temperature=0.2,
            max_tokens=8192,
        )

    async def arun(
        self,
        module_title: str,
        ast: Dict[str, Any],
        description: str,
        fixes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return await self.acall_llm_json(
            self._build_prompt(module_title, ast, description, fixes),
            temperature=0.2,
            max_tokens=8192,
        )

    @staticmethod
    def _build_prompt(module_title: str, ast: Dict[str, Any], description: str, fixes: Optional[List[str]] = None) -> str:
        prompt = (
            f"<module_name>{module_title}</module_name>\n\n"
            f"<ast>\n{json.dumps(ast, indent=2)}\n</ast>\n\n"
            f"<description>\n{description}\n</description>"
        )
        if fixes:
            prompt += "\n\n**CRITIC FEEDBACK FROM PREVIOUS ATTEMPT — address every point:**\n"
            for i, fix in enumerate(fixes, 1):
                prompt += f"{i}. {fix}\n"
        return prompt

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
