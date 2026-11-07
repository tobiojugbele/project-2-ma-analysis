# Project Decisions Journal

* **Decision:** Segmented New York state layers into structural Metro/Upstate buckets, and isolated the risk-to-quality regression matrix inside a single insurer contract line.
* **Why:** Model Segmentation isolates downstate funding variations, and the confounding check tests if our aggregate findings are driven by a true systemic driver or simply skewed by insurer size differences.

### 2026-11-03: Structural Segmentation & Insurer Confounding Audits
* **Decision:** Segmented New York state layers into structural Metro/Upstate buckets, and isolated the risk-to-quality regression matrix inside a single insurer contract line.
* **Why:** Model Segmentation isolates downstate funding variations, and the confounding check tests if our aggregate findings are driven by a true systemic driver or simply skewed by insurer size differences.

### 2026-11-04: Business Intelligence Frontend Semantic Layering
* **Decision:** Built out executive report layouts in Power BI utilizing takeaway titles, filled maps, and insurer-isolated scatter plots.
* **Why:** Replaces plain descriptive labels with clear conclusions, allowing non-technical stakeholders to explore the data and see how insurer size confounds overall risk trends.

### 2026-11-05: Quality Bonus Payment (QBP) Financial Modeling
* **Decision:** Built a multi-scenario revenue-at-risk simulation engine (Low 3%, Base 5%, High 7%) based on 2027 CMS Stars and 2027 County Ratebooks. Incorporated a +0.5 star parameter shift slider.
* **Why:** Translates operational quality scores directly into financial impact metrics, mimicking how managed care finance teams model bid risk and margin exposure.

### 2026-11-06: Production Documentation Release & Limitations Audit
* **Decision:** Released Project 1 v1.0 with structured findings and documented Project 2 data constraints (HHI metrics, 11-member cell masking thresholds, and confounding factors).
* **Why:** Aligns the repositories with professional software standards, ensuring data definitions and limitations are clearly communicated to reviewers.
