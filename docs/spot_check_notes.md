# Day 3 Relational Join & Spot-Validation Log

### 1. Ingestion Audit and Join Drop Metrics
* **Join 1 (Enrollment + Stars):** Maintained 100% of base tracking records. No contract drops observed.
* **Join 2 (Geographic Penetration Integration):** Inner join restricted dataset cleanly to target state constraints. Out-of-scope regions dropped as expected.
* **Join 3 (Ratebook Integration):** Confirmed all 5-digit county FIPS codes matched exactly. 0 keys were left unmatched.

### 2. Manual Source File Spot-Validation Check
* Verified random rows from `data/medicare.db` directly against raw sheets.
* Padded FIPS codes (`36059`), enrollment metrics, and contract indicators match original federal sources exactly. No cell values were shifted or broken during data extraction.
