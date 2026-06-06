import os
import json
import asyncio
from typing import Any, Dict, List, Optional

from test_case_generation.framework.agents.post_verifier import StateChangeAgent, PostVerificationAgent

class PostVerificationGenerator:
    def __init__(
        self,
        api_key: str,
        model: str = "openai/gpt-4o",
        debug: bool = False,
        debug_file: str = "debug_log.txt",
    ):
        self.api_key = api_key
        self.model = model
        self.debug = debug
        self.debug_file = debug_file
        self.debug_dir = ""

        self.gate_agent = StateChangeAgent(api_key=api_key, model=model, debug=debug, debug_file=debug_file)
        self.verify_agent = PostVerificationAgent(api_key=api_key, model=model, debug=debug, debug_file=debug_file)

    async def generate(
        self,
        merged_description: str,
        test_cases: List[Dict[str, Any]],
        output_dir: str = "output",
    ) -> List[Dict[str, Any]]:
        print("=" * 60)
        print("TEST CASE GENERATION  (Post-Verification Pipeline)")
        print("=" * 60)
        print(f"Processing {len(test_cases)} test cases...")

        os.makedirs(output_dir, exist_ok=True)
        if self.debug:
            self.debug_dir = os.path.join(output_dir, "debug")
            os.makedirs(self.debug_dir, exist_ok=True)

        post_verifications = []

        # Process each test case concurrently (with limited concurrency handled by BaseAgent)
        tasks = []
        for tc in test_cases:
            tasks.append(self._process_single_test_case(merged_description, tc))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for res in results:
            if isinstance(res, dict) and res:
                post_verifications.append(res)
            elif isinstance(res, Exception):
                print(f"Error processing a test case: {res}")

        # Write the final output
        out_path = os.path.join(output_dir, "post-verifications.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(post_verifications, f, indent=2)

        print(f"Generated {len(post_verifications)} post-verifications.")
        print(f"Saved to: {out_path}")
        return post_verifications

    async def _process_single_test_case(self, description: str, tc: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        # Step 1: Gate
        try:
            gate_res = await self.gate_agent.arun(test_case=tc)
        except Exception as e:
            print(f"Gate evaluation failed for tc_id {tc.get('tc_id')}: {e}")
            return None

        if not gate_res.get("requires_post_verification", False):
            # No verification needed
            return None

        print(f"Generating post-verification for {tc.get('tc_id')} (Reason: {gate_res.get('reason')})")

        # Step 2: Generate Schema
        try:
            verify_res = await self.verify_agent.arun(description=description, test_case=tc)
        except Exception as e:
            print(f"Post-verification generation failed for tc_id {tc.get('tc_id')}: {e}")
            return None

        return verify_res
