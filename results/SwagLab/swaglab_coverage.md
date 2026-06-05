# SwagLab — Test-Case Coverage Report

> **Ground Truth:** 82 TCs across 9 modules · [`swaglab.md`](file:///d:/Test-Case-Generator/dataset/ground_truth/swaglab.md)  
> **Raw Specification:** 9 modules · [`SwagLab.md`](file:///d:/Test-Case-Generator/dataset/raw_specifications/SwagLab/SwagLab.md)  
> **Evaluated:** 2 models × 5 approaches = 10 suites · [`results/SwagLab/`](file:///d:/Test-Case-Generator/results/SwagLab/)  
> **Date:** 2026-06-05

---

## 1. Raw Test Case Counts (Module by Module)

The table below shows the exact number of test cases generated per official module. For flat approaches (zero_shot, few_shot), each test case was individually inspected and assigned to a module based on its title and content.

> **ZS** = zero_shot · **ZS/M** = zero_shot_per_module · **FS** = few_shot · **FS/M** = few_shot_per_module · **AG** = agent

| Module | GT | 4o · ZS | 4o · ZS/M | 4o · FS | 4o · FS/M | 4o · Agent | 5 · ZS | 5 · ZS/M | 5 · FS | 5 · FS/M | 5 · Agent |
|---|:--:|:-------:|:---------:|:-------:|:---------:|:----------:|:------:|:--------:|:------:|:--------:|:---------:|
| Login | 15 | 4 | 8 | 3 | 7 | 12 | 5 | 16 | 5 | 12 | 15 |
| Product Inventory | 17 | 1 | 8 | 1 | 4 | 11 | 3 | 12 | 4 | 12 | 11 |
| Product Detail | 7 | 0 | 6 | 0 | 4 | 9 | 1 | 14 | 1 | 10 | 11 |
| Shopping Cart | 10 | 1 | 7 | 1 | 5 | 8 | 2 | 11 | 2 | 8 | 8 |
| Checkout – Information | 12 | 1 | 7 | 1 | 6 | 11 | 4 | 10 | 3 | 8 | 14 |
| Checkout – Overview | 9 | 1 | 5 | 1 | 3 | 6 | 2 | 12 | 1 | 7 | 8 |
| Checkout – Confirmation | 5 | 1 | 5 | 1 | 3 | 3 | 1 | 10 | 1 | 7 | 8 |
| Logout | 4 | 1 | 4 | 1 | 3 | 4 | 2 | 10 | 2 | 8 | 9 |
| Reset App State | 3 | 0 | 4 | 0 | 3 | 2 | 2 | 10 | 1 | 10 | 8 |
| **Suite Total** | **82** | **10** | **54** | **9** | **38** | **66** | **22** | **105** | **20** | **82** | **92** |

> Modules with 0 TCs in flat approaches indicate the model collapsed coverage onto higher-priority modules and generated no tests for those areas at all.

---

## 2. Critical Business Rules (15 tracked)

The 15 rules below were extracted from the raw SwagLab specification and represent the most critical, application-specific behaviours. Each is a precise, verifiable condition.

| # | Business Rule | 4o · ZS | 4o · ZS/M | 4o · FS | 4o · FS/M | 4o · Agent | 5 · ZS | 5 · ZS/M | 5 · FS | 5 · FS/M | 5 · Agent |
|:-:|---|:-------:|:---------:|:-------:|:---------:|:----------:|:------:|:--------:|:------:|:--------:|:---------:|
| 1 | `locked_out_user` credentials show the exact error message "Sorry, this user has been locked out" | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 2 | Submitting login with an empty username field shows the inline error "Epic sadface: Username is required" | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 3 | Submitting login with an empty password field shows the inline error "Epic sadface: Password is required" | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 4 | Usernames are case-sensitive — `standard_user` succeeds but `Standard_User` fails | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 5 | The default product sort order on the inventory page is "Name (A to Z)" | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 6 | All four sort options (A–Z, Z–A, Price Low–High, Price High–Low) correctly reorder the product list | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 7 | Clicking "Add to cart" changes the button label to "Remove" and increments the cart badge counter | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 8 | Clicking "Remove" changes the button label back to "Add to cart" and decrements the cart badge counter | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 9 | Cart contents persist when navigating away from the cart page and returning | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | ✓ |
| 10 | Proceeding to checkout with an empty First Name field shows the inline error "Error: First Name is required" | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 11 | Proceeding to checkout with an empty Last Name field shows the inline error "Error: Last Name is required" | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 12 | Proceeding to checkout with an empty Postal Code field shows the inline error "Error: Postal Code is required" | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 13 | The checkout overview page displays the tax amount calculated at exactly 8% of the subtotal | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| 14 | Completing a purchase shows the confirmation message "Thank you for your order!" | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| 15 | The "Reset App State" sidebar link clears the cart and reverts all "Remove" buttons to "Add to cart" | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ |
| | **Rules Covered** | **3 / 15** | **12 / 15** | **2 / 15** | **10 / 15** | **15 / 15** | **8 / 15** | **15 / 15** | **4 / 15** | **12 / 15** | **15 / 15** |

Three approaches achieve perfect recall (15/15): both agent-based approaches and `gpt-5-mini / ZS/M`. Flat approaches peak at 8/15, demonstrating that unstructured generation misses deep, module-specific behaviours.

---

## 3. Composite Scores & Final Ranking

The final composite score ($S$) is computed using a strict $0.40 / 0.60$ weighting between symmetric volume calibration ($C_{breadth}$) and business rule depth ($R_{br}$). Over-generation is penalised exactly as harshly as under-generation.
- $C_{breadth} = 100 \times \frac{\min(TC_{gen}, TC_{GT})}{\max(TC_{gen}, TC_{GT})}$
- $R_{br} = 100 \times \frac{BR_{caught}}{BR_{total}}$
- **$S = 0.40 \times C_{breadth} + 0.60 \times R_{br}$**

> Ground Truth Baseline: **82 TCs · 15 business rules**

### 🏆 Verdict

**Winner: `gpt-5-mini / agent`** — composite score **95.7 / 100**. It achieves perfect business rule recall (15/15) with 92 TCs generated — just 10 more than the GT baseline, resulting in the highest $C_{breadth}$ (89.1) of all approaches achieving perfect depth.

The key discriminating pattern in this dataset: the metric clearly separates the three 15/15 approaches — `gpt-5-mini / agent` wins over `gpt-4o-mini / agent` (+3.5 pts) because the budget model under-generates (66 TCs), and over `gpt-5-mini / ZS/M` (+4.5 pts) because ZS/M over-generates (105 TCs). **Calibrated volume, not maximum volume, is the winning strategy.**

| Rank | Approach | TCs | BRs | $C_{breadth}$ | $R_{br}$ | **Score $S$** | Diff | Recommended Use Case |
|:----:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 1st | gpt-5-mini · Agent | 92 | 15 / 15 | 89.1 | 100.0 | **95.7** | - | Production regression suite — best balance of volume and depth |
| 🥈 2nd | gpt-4o-mini · Agent | 66 | 15 / 15 | 80.5 | 100.0 | **92.2** | -3.5 | Budget-constrained projects requiring maximum rule depth |
| 🥉 3rd | gpt-5-mini · ZS/M | 105 | 15 / 15 | 78.1 | 100.0 | **91.2** | -4.5 | Cost-efficient alternative; slight over-generation penalty |
| 4th | gpt-5-mini · FS/M | 82 | 12 / 15 | 100.0 | 80.0 | **88.0** | -7.7 | When agent is unavailable; volume is perfect but 3 rules missed |
| 5th | gpt-4o-mini · ZS/M | 54 | 12 / 15 | 65.9 | 80.0 | **74.3** | -21.4 | Lightweight structured baseline; acceptable for initial coverage |
| 6th | gpt-4o-mini · FS/M | 38 | 10 / 15 | 46.3 | 66.7 | **58.5** | -37.2 | Minimal smoke testing only; significant rule gaps |
| 7th | gpt-5-mini · ZS | 22 | 8 / 15 | 26.8 | 53.3 | **42.7** | -53.0 | Not recommended — insufficient volume and rule depth |
| 8th | gpt-5-mini · FS | 20 | 4 / 15 | 24.4 | 26.7 | **25.8** | -69.9 | Not recommended — very low rule recall |
| 9th | gpt-4o-mini · ZS | 10 | 3 / 15 | 12.2 | 20.0 | **16.9** | -78.8 | Avoid — coverage collapse; only 4 of 9 modules represented |
| 10th | gpt-4o-mini · FS | 9 | 2 / 15 | 11.0 | 13.3 | **12.4** | -83.3 | Avoid — near-zero coverage; unacceptable for any QA purpose |

> [!WARNING]
> All four flat approaches (zero_shot and few_shot for both models) generate fewer than 25 TCs against an 82-TC ground truth. Product Detail receives **zero tests** from both flat models, leaving an entire module completely untested. These approaches should never be used for multi-module web applications.
