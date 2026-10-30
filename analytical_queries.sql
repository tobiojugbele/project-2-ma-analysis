-- QUERY 1: County Benchmarks & PMPM Financial Approximations (Q4/Q5)
SELECT 
    county_fips,
    county,
    base_rate as annualized_county_benchmark,
    (base_rate / 12.0) as calculated_pmpm_benchmark
FROM ny_market_analysis
GROUP BY county_fips;
