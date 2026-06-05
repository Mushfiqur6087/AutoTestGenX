# Test-Case Coverage Evaluation Workflow

This plan outlines the rigorous, mathematically sound process for auditing and generating test-case coverage reports for any dataset. It serves as the universal blueprint for ensuring an apples-to-apples academic comparison across all evaluated web applications.

## Purpose

The goal of this evaluation is to determine the most effective LLM test generation strategy (`gpt-4o-mini` vs `gpt-5-mini` across `zero_shot`, `few_shot`, `per_module`, and `agent` approaches). 

We employ a rigorous **Academic Standard** that **penalizes over-generation (test spam)** and heavily weights the capture of critical business logic, effectively ensuring that the generated test cases are both broad and deep.

---

## 1. Ground Truth (GT) Alignment
To ensure a fair baseline, the Ground Truth must perfectly mirror the raw specification.
- **Source Specification**: `dataset/raw_specifications/[Dataset]/[Dataset].md`
- **Target Ground Truth**: `dataset/ground_truth/[dataset].md`
- **Rename**: Align GT module headers to the raw spec exactly (e.g. `## Login`).
- **Prune**: Delete any human-added modules not present in the raw spec (e.g., E2E sequences, generic navigation).
- **Truncate**: Remove all extraneous text and recalculate the GT TC/Module totals at the bottom of the file.

## 2. Business Rule Extraction
- **Source Specification**: `dataset/raw_specifications/[Dataset]/[Dataset].md`
- Identify 15–20 critical, deeply specific business rules from the raw spec (e.g., specific boundaries, interdependent field validation, state resets).
- Record these rules to be used as a qualitative checklist during the generation audit.

## 3. Raw Generation Audit
- **Target Generation Files**: `results/[Dataset]/[model]/[approach]/test-cases.json`
- Script the parsing of all 10 `test-cases.json` files for the dataset.
- Extract the exact number of test cases generated ($TC_{gen}$) globally and per module for each approach.
- Manually or programmatically audit the JSON outputs to record which approaches successfully generated tests covering the specific business rules extracted in Step 2.

## 4. Academic Metric Calculation
Calculate the composite score ($S$) for all approaches using the rigorous two-component Academic Standard formula:

### The Formula: $\boxed{S = 0.40\,C_{breadth} + 0.60\,R_{br}}$

1. **Volume Calibration ($C_{breadth}$)**: Evaluates symmetric coverage, penalizing both under-generation and over-generation naturally.
   $C_{breadth} = 100 \times \frac{\min(TC_{gen}, TC_{GT})}{\max(TC_{gen}, TC_{GT})}$

2. **Business Rule Recall ($R_{br}$)**: Rewards deep, accurate testing of the actual business logic.
   $R_{br} = \frac{BR_{caught}}{BR_{total}} \times 100$

*(Note: Module coverage is excluded from the formula because well-structured approaches universally achieve 100% module coverage, making it a poor discriminator).*

## 5. Report Generation
- **Target Output File**: `results/[Dataset]/[dataset]_coverage.md`

Generate the final coverage report ensuring it exactly mirrors the established structure. It MUST contain the following 3 sections:
1. **Raw Test Case Counts (Module by Module)**: A granular table showing the raw number of generated TC counts per module. Flat approaches MUST be manually mapped.
2. **Critical Business Rules (X tracked)**: The precise, full-sentence boolean checklist of qualitative rule hits.
3. **Composite Scores & Final Ranking**: Briefly mention the $S = 0.40 C_{breadth} + 0.60 R_{br}$ metrics. State the verdict based on the highest $S$ score, and present the master ranking table including columns for TCs, BRs, metrics, Score $S$, Diff from winner, and Usage Recommendations.
