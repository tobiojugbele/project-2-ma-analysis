import os
import sqlite3
import pandas as pd

def run_project2_market_structure():
    print("🚀 Project 2 SQL: Computing Herfindahl-Hirschman Index (HHI) Concentration...")
    db_path = "data/medicare.db"
    out_dir = "data/processed"
    os.makedirs(out_dir, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    
    # --- QUERY 1: HHI Market Share Concentration & Top-3 Insurer Share (Q4) ---
    print("📊 Evaluating county market concentration indexes...")
    hhi_sql = """
    -- Why: Computes HHI by squaring individual contract enrollment shares inside each county area grid.
    WITH county_totals AS (
        SELECT county_fips, county, SUM(enrollment) as total_county_enrollment
        FROM ny_market_analysis
        GROUP BY county_fips
    ),
    shares AS (
        SELECT 
            a.county_fips,
            a.county,
            a.contract_id,
            a.enrollment,
            (cast(a.enrollment as float) / b.total_county_enrollment) * 100.0 as market_share
        FROM ny_market_analysis a
        JOIN county_totals b ON a.county_fips = b.county_fips
        WHERE b.total_county_enrollment > 0
    )
    SELECT 
        county_fips,
        county,
        SUM(market_share * market_share) as herfindahl_hirschman_index,
        SUM(CASE WHEN row_num <= 3 THEN market_share ELSE 0 END) as top_3_market_share_percent
    FROM (
        SELECT *, ROW_NUMBER() OVER(PARTITION BY county_fips ORDER BY enrollment DESC) as row_num
        FROM shares
    )
    GROUP BY county_fips;
    """
    df_hhi = pd.read_sql_query(hhi_sql, conn)
    df_hhi.to_csv(os.path.join(out_dir, "q4_market_structure_hhi.csv"), index=False)
    
    # --- QUERY 2: Federal Benchmark Rates vs County Penetration Models ---
    print("📊 Evaluating Benchmark vs Penetration correlation vectors...")
    bench_sql = """
    -- Why: Maps financial base rates directly to regional penetration to see if funding drives enrollment.
    SELECT 
        county_fips,
        county,
        AVG(base_rate) as local_county_benchmark_rate,
        AVG(enrollment) as active_enrollment_volume
    FROM ny_market_analysis
    GROUP BY county_fips;
    """
    df_bench = pd.read_sql_query(bench_sql, conn)
    df_bench.to_csv(os.path.join(out_dir, "q4_benchmark_vs_penetration.csv"), index=False)
    
    conn.close()
    print("🎉 Project 2 market structure handoff reporting CSV files generated successfully.")

if __name__ == "__main__":
    run_project2_market_structure()
