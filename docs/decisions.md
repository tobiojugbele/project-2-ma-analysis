# Project 2 Analytics Governance Registry

### 1. Processing Granularity Boundary
* **Decision:** The transformation runtime executes analysis at the **Contract-Level** granularity.
* **Why:** High-level county summaries mask the variance in star performance across plan options. Aggregating calculations at the contract identifier level preserves the accuracy of performance ranges within a single geographic region.

### 2. Cell Suppression Security Limits (Values Under 11)
* **Decision:** CMS cell counts showing enrollment values between 1 and 10 are completely masked and flagged with a distinct numerical proxy value of `NaN`.
* **Why:** This mirrors federal data privacy rules to protect patient anonymity in low-volume areas.

### 3. Analytics Horizon Year Mapping Matrix
* **Decision:** Datasets are joined according to the following staggered release calendar pairings:
  * **2027 Star Performance Ratings** map directly to **CY 2027 County Ratebook Benchmarks**.
  * **2026/2025 Penetration Records** trace the current-to-prior base enrollment metrics.
* **Why:** Star Ratings and Ratebooks are forward-looking tables published ahead of the operational tracking year. Staggering them this way aligns a plan's quality ratings with the actual payment benchmarks it received for that performance period.
