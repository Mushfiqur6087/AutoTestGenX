# ParaBank — Test-Case Coverage Report

> **Ground Truth:** 169 TCs across 13 modules · [`Parabank.md`](file:///d:/Test-Case-Generator/dataset/ground_truth/Parabank.md)  
> **Raw Specification:** 13 modules · [`Parabank.md`](file:///d:/Test-Case-Generator/dataset/raw_specifications/Parabank/Parabank.md)  
> **Evaluated:** 2 models × 5 approaches = 10 suites · [`results/Parabank/`](file:///d:/Test-Case-Generator/results/Parabank/)  
> **Date:** 2026-06-05

---

## 1. Raw Test Case Counts (Module by Module)

The table below shows the exact number of test cases generated per official module. For flat approaches (zero_shot, few_shot), each test case was individually inspected and assigned to a module based on its title and content.

> **ZS** = zero_shot · **ZS/M** = zero_shot_per_module · **FS** = few_shot · **FS/M** = few_shot_per_module · **AG** = agent

| Module | GT | 4o · ZS | 4o · ZS/M | 4o · FS | 4o · FS/M | 4o · Agent | 5 · ZS | 5 · ZS/M | 5 · FS | 5 · FS/M | 5 · Agent |
|---|:--:|:-------:|:---------:|:-------:|:---------:|:----------:|:------:|:--------:|:------:|:--------:|:---------:|
| Login | 12 | 3 | 7 | 3 | 5 | 12 | 4 | 14 | 4 | 12 | 12 |
| Register | 23 | 3 | 9 | 3 | 5 | 19 | 6 | 20 | 5 | 15 | 22 |
| Accounts Overview | 6 | 0 | 7 | 0 | 4 | 4 | 2 | 12 | 1 | 9 | 13 |
| Open New Account | 12 | 0 | 8 | 3 | 7 | 15 | 3 | 15 | 3 | 13 | 19 |
| Transfer Funds | 14 | 3 | 7 | 2 | 6 | 13 | 4 | 15 | 4 | 10 | 19 |
| Payments | 15 | 3 | 6 | 0 | 4 | 17 | 3 | 13 | 3 | 14 | 14 |
| Request Loan | 18 | 3 | 7 | 0 | 5 | 20 | 3 | 14 | 3 | 13 | 32 |
| Update Contact Info | 18 | 3 | 5 | 0 | 4 | 12 | 2 | 15 | 2 | 10 | 12 |
| Manage Cards | 10 | 3 | 8 | 0 | 6 | 18 | 1 | 16 | 2 | 16 | 18 |
| Investments | 13 | 3 | 8 | 0 | 7 | 16 | 3 | 20 | 3 | 11 | 20 |
| Account Statements | 9 | 3 | 7 | 1 | 6 | 10 | 2 | 13 | 2 | 10 | 19 |
| Security Settings | 8 | 3 | 6 | 0 | 5 | 10 | 2 | 12 | 2 | 11 | 11 |
| Support Center | 11 | 6 | 7 | 0 | 7 | 14 | 3 | 19 | 2 | 14 | 19 |
| **Suite Total** | **169** | **36** | **92** | **12** | **71** | **180** | **30** | **198** | **32** | **158** | **230** |

> Modules with 0 TCs in flat approaches indicate the model collapsed coverage onto other modules and generated no tests for those areas at all. `gpt-4o-mini / FS` covers only 5 of 13 modules.

---

## 2. Critical Business Rules (20 tracked)

The 20 rules below were extracted from the raw ParaBank specification and represent the most critical, application-specific behaviours covering authentication, form validation, financial logic, and account management.

| # | Business Rule | 4o · ZS | 4o · ZS/M | 4o · FS | 4o · FS/M | 4o · Agent | 5 · ZS | 5 · ZS/M | 5 · FS | 5 · FS/M | 5 · Agent |
|:-:|---|:-------:|:---------:|:-------:|:---------:|:----------:|:------:|:--------:|:------:|:--------:|:---------:|
| 1 | Entering an incorrect password clears the password field but retains the username for correction | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | Registration enforces all 4 password complexity rules: minimum length, uppercase, number, and special character | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 3 | The phone number field auto-formats input into the `(XXX) XXX-XXXX` pattern as the user types | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | The SSN field auto-formats input into the `XXX-XX-XXXX` pattern as the user types | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 5 | The ZIP code field accepts both 5-digit and ZIP+4 (`XXXXX-XXXX`) formats | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 6 | The accounts overview page displays a running total balance footer summing all account balances | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 7 | Accounts on the overview page are sorted in chronological order of creation date | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 8 | Opening a new Checking account requires a minimum initial deposit of $25 | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ |
| 9 | Opening a new Savings account requires a minimum initial deposit of $100 | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 10 | Transferring funds to the same account as the source account is blocked with an appropriate error | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 11 | Adding an external account requires the routing number and account number to match exactly | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 12 | The bill payment form supports quick-select from existing registered payees | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 13 | The loan application page displays the current APR for each loan type before submission | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 14 | A loan application is denied if the requested down payment is less than the required amount | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 15 | A loan application is denied if the collateral value is below 20% of the requested loan amount | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16 | A card can be frozen and subsequently unfrozen, restoring its active status | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 17 | Selling more shares than the user currently owns is blocked with an insufficient-holdings error | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 18 | The user can opt in to paperless statements and this preference is persisted on the next page load | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 19 | Changing the account password requires entering the correct current password; an incorrect current password is rejected | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ |
| 20 | The support callback form validates that the requested callback date is not in the past | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ |
| | **Rules Covered** | **2 / 20** | **11 / 20** | **3 / 20** | **13 / 20** | **20 / 20** | **9 / 20** | **20 / 20** | **8 / 20** | **20 / 20** | **20 / 20** |

Four approaches achieve perfect recall (20/20): both agent-based approaches and both per-module variants of `gpt-5-mini`. Flat approaches peak at 9/20, demonstrating that unstructured generation cannot explore the full depth of a 13-module banking application.

---

## 3. Composite Scores & Final Ranking

The final composite score ($S$) is computed using a strict $0.40 / 0.60$ weighting between symmetric volume calibration ($C_{breadth}$) and business rule depth ($R_{br}$). Over-generation is penalised exactly as harshly as under-generation.
- $C_{breadth} = 100 \times \frac{\min(TC_{gen}, TC_{GT})}{\max(TC_{gen}, TC_{GT})}$
- $R_{br} = 100 \times \frac{BR_{caught}}{BR_{total}}$
- **$S = 0.40 \times C_{breadth} + 0.60 \times R_{br}$**

> Ground Truth Baseline: **169 TCs · 20 business rules**

### 🏆 Verdict

**Winner: `gpt-4o-mini / agent`** — composite score **97.6 / 100**. It achieves perfect business rule recall (20/20) with 180 TCs generated — only 11 more than the GT baseline, resulting in a $C_{breadth}$ of 93.9, the highest among all approaches with perfect depth.

This is a **major finding**: a budget-tier model outscored the most capable model (`gpt-5-mini / agent`, 89.4) because the more powerful model **over-generated by 61 TCs** (230 vs 169), incurring a severe breadth penalty despite identical business rule recall. The agent framework, not raw model capability, is the deciding factor — it enables `gpt-4o-mini` to discover every critical business rule while staying calibrated to the GT volume.

| Rank | Approach | TCs | BRs | $C_{breadth}$ | $R_{br}$ | **Score $S$** | Diff | Recommended Use Case |
|:----:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 1st | gpt-4o-mini · Agent | 180 | 20 / 20 | 93.9 | 100.0 | **97.6** | - | Production regression suite — best balance of volume and depth |
| 🥈 2nd | gpt-5-mini · FS/M | 158 | 20 / 20 | 93.5 | 100.0 | **97.4** | -0.2 | When agent is unavailable; strong model, well-calibrated volume |
| 🥉 3rd | gpt-5-mini · ZS/M | 198 | 20 / 20 | 85.4 | 100.0 | **94.1** | -3.5 | Cost-efficient; slight over-generation penalty accepted |
| 4th | gpt-5-mini · Agent | 230 | 20 / 20 | 73.5 | 100.0 | **89.4** | -8.2 | Perfect depth but heavily penalised for 61-TC over-generation |
| 5th | gpt-4o-mini · FS/M | 71 | 13 / 20 | 42.0 | 65.0 | **55.8** | -41.8 | Smoke testing only; 7 business rules missed |
| 6th | gpt-4o-mini · ZS/M | 92 | 11 / 20 | 54.4 | 55.0 | **54.8** | -42.8 | Lightweight structured baseline; significant rule gaps |
| 7th | gpt-5-mini · ZS | 30 | 9 / 20 | 17.8 | 45.0 | **34.1** | -63.5 | Not recommended — insufficient volume and rule depth |
| 8th | gpt-5-mini · FS | 32 | 8 / 20 | 18.9 | 40.0 | **31.6** | -66.0 | Not recommended — very low rule recall |
| 9th | gpt-4o-mini · ZS | 36 | 2 / 20 | 21.3 | 10.0 | **14.5** | -83.1 | Avoid — coverage collapse; 5 of 13 modules receive zero tests |
| 10th | gpt-4o-mini · FS | 12 | 3 / 20 | 7.1 | 15.0 | **11.8** | -85.8 | Avoid — near-zero coverage; only 5 modules reached |

> [!WARNING]
> All four flat approaches generate fewer than 37 TCs against a 169-TC ground truth. `gpt-4o-mini / FS` reaches only 5 of 13 modules, leaving Accounts Overview, Payments, Request Loan, Update Contact Info, Manage Cards, Investments, Security Settings, and Support Center with **zero test cases**. Never use flat approaches for multi-module applications.
