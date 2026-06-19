"""Negative Test Case Agent: generates invalid-input and constraint-violation test cases from a Structural Model."""

from importlib import resources
from typing import Any, Dict, List, Optional

from test_generation.framework.agents.base import BaseAgent
from test_generation.framework.agents.utils import build_test_prompt

_PROMPT = resources.files("test_generation.prompts").joinpath("negative_test_case_generator.md").read_text(encoding="utf-8")


class NegativeTestCaseGeneratorAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "Test-Negative"

    @property
    def system_prompt(self) -> str:
        return _PROMPT

    def run(self, module_title: str, ast: Dict[str, Any], description: str, workflows: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        return self.call_llm_json(
            build_test_prompt(module_title, ast, description, workflows),
            temperature=0.3,
            max_tokens=16384,
        )

    async def arun(self, module_title: str, ast: Dict[str, Any], description: str, workflows: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        return await self.acall_llm_json(
            build_test_prompt(module_title, ast, description, workflows),
            temperature=0.3,
            max_tokens=16384,
        )
