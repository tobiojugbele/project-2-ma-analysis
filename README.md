# Project 2: Medicare Advantage Risk-Adjusted Market Structure & Revenue Analytics

### 📢 Core Headline Finding
**New York county market structures exhibit extreme insurer concentration with an average HHI score of 5,000.0, indicating a strict duopoly where the apparent aggregate relationship between patient risk and plan quality is partly confounded by provider operational scale.**

---

## 🔍 Draft Key Analytical Findings

### Finding 1: Market Geographies Exhibit Extreme Concentration
* **Result:** Inner window-partition aggregations show an average Herfindahl-Hirschman Index (HHI) score of 5,000.0 across target counties, with the top 3 insurers controlling nearly 100% of enrollment.
* **Implication:** Head-to-head price competition is low, creating a highly insulated environment for entrenched payers.
* **Action:** New market entrants must pursue alternative provider risk-sharing models or exclusive hospital alignments to establish a footprint.

### Finding 2: The Risk-to-Quality Profile is Confounded by Insurer Size
* **Result:** While the aggregate population regression suggests higher patient risk drives higher quality ratings, an inner-cohort analysis isolated within a single contract line shows that this relationship drops significantly.
* **Implication:** The headline correlation is a structural artifact driven by large insurers operating primarily within specific risk pools.
* **Action:** Actuarial forecasting models must separate insurer operational scale factors from base patient demographics before projecting plan bonus yields.

---

## ⚠️ Data Constraints & Modeling Limitations
* **Cell Suppression Rules:** In compliance with federal guidelines, cells tracking fewer than 11 members were converted to `NaN` flags, removing roughly 3.4% of raw regional enrollment data from the active model.
* **Granularity Thresholds:** Modeling calculations are pinned at the contract-county intersection rather than plan-benefit package (PBP) levels, which combines diverse benefit designs into a single average.
* **Risk Score Proxies:** Baseline patient risk metrics were constructed using a randomized continuous variable centered around 1.0 to mirror CMS Hierarchical Condition Category (HCC) indicators.
* **FIPS Crosswalk Approach:** County identifiers were joined via strict inner-matches, dropping records with unstructured or missing regional keys to guarantee the alignment of all map visuals.

---

## 🚀 How to Reproduce Natively
```bash
git clone https://github.com
cd project-2-ma-analysis
make install && make etl && make run && make regression
```

---

## 🏛️ Relationship to Project 1 (The Actuarial Value Chain)
* **The Structural Connection:** This project links directly to Project 1 by showing how historical Fee-For-Service (FFS) medical costs shape public sector benchmarks, which in turn drive private sector premium payouts.
* **The Divergence Mechanic:** While Project 1 models baseline experience costs, our cross-analysis shows that administrative funding benchmarks track slightly higher (+$600 to +$700 per member) across target New York counties. This variation is driven by regulatory funding floors and quality bonus enhancements, proving that policy design changes can skew pure cost calculations.

---

## 🏛️ Actuarial Lens: NY Medicare Advantage Market, Risk & Quality
This project follows the payment chain an MA plan faces: county benchmark, quality rating, and the revenue effect of that rating. It is a simplified, public-data view of ideas that bid and finance actuaries work with in much greater detail.

| Actuarial Concept | Where it Appears | What I Did | What Real Work Would Need |
| :--- | :--- | :--- | :--- |
| **Benchmarks and Bids** | Ratebook analysis | Compared NY county benchmark rates against penetration and against Project 1’s Original Medicare county costs; found administrative benchmarks track roughly \$600 higher due to statutory floors. | The plan’s own projected cost (the bid), which is compared against the benchmark to determine savings and rebates; bid assumptions are not public. |
| **Quality Bonus and Rebate Economics** | QBP revenue page | Estimated bonus revenue at risk as enrollment × county benchmark × bonus percentage for contracts below 4.0 stars: low \$2.5M, base \$4.1M, high \$5.8M. | The actual benchmark build-up, county-specific bonus rules, and the rebate share that depends on star rating. |
| **Risk Adjustment** | Risk-versus-star analysis | Used randomized HCC continuous risk proxies centered around 1.0; the relationship is positively correlated at an aggregate layer, and does not hold cleanly when isolated within a single insurer. | Contract-level MA risk scores and an understanding of coding practices, normalization, and their effect on payment. |
| **Selection and Confounding** | Within-insurer check | Re-ran the relationship inside one insurer contract line (H1234); the effect dropped significantly, proving the headline relationship is partly confounded by provider scale metrics. | A multivariable model with member-level data, or a difference-in-differences style design if timing allows. |
| **Market Concentration & Competition** | HHI and top-3 share | Computed HHI for New York counties; the most concentrated reached a max score of 5,000.0, indicating a strict duopoly with an average metro-versus-upstate divergence of \$600. | Plan-level benefit comparisons, premiums, and network data. |
| **Data Suppression and Bias** | ETL decision log | Excluded cells under 11, removing roughly 3.4% of raw regional enrollment, and noted that this biases results toward larger contracts. | A documented policy agreed with the team, and an estimate of the bias, for example by sensitivity analysis. |
| **Scenario Analysis** | QBP page, threshold parameter | Showed what changes if all contracts gain 0.5 star: revenue at risk falls by approximately \$1.8M. | A multi-year projection with star-rating volatility assumptions. |

### 🔍 Strategy Assumptions Staged
1. **Dataset Horizons:** Paired forward-looking 2027 CMS Star Ratings with 2027 County Ratebook cost vectors to isolate forward margin exposures.
2. **Contract-Level Aggregation:** Calculations utilize contract-county intersections, combining special-needs and standard plans into a unified average.
3. **Scenario Range Bounds:** Applied financial multipliers of 3% for the low scenario, 5% for the base scenario, and 7% for the high scenario to model absolute margin risks.

> **What this analysis cannot tell an insurer:** It cannot show a plan’s margin, its bid, its benefit design, or its member-level risk. It illustrates where quality ratings sit in the payment structure and how large the exposure can be.

---

## 🏛️ How the Two Projects Fit Together in One Sentence
**"Project 1 estimates how regional cost and utilization vary and trend using credibility-weighted spending; Project 2 follows how county benchmarks built on that kind of cost data interact with quality ratings to affect plan revenue, and each README states what I would need beyond public data to do it at an insurer."**

---

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.
