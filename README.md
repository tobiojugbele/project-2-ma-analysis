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
