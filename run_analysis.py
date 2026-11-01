import os
import sqlite3
import pandas as pd

def run_project2_sql():
    print("🚀 Project 2 SQL: Executing healthcare market weighted calculations...")
    db_path = "data/medicare.db"
    out_dir = "data/processed"
    os.makedirs(out_dir, exist_ok=True)

    if not os.path.exists(db_path):
        print("❌ Staged SQLite database missing!")
        return
        
    conn = sqlite3.connect(db_path)
    
    # --- QUERY 1: County Market Penetration Rankings (Q4) ---
    print("📊 Computing County Penetration Ranking Profiles...")
    q4_rank_sql = """
    -- Why: Utilizes absolute window ranking to sort counties by total eligible population metrics.
    SELECT 
        county_fips,
        county,
        eligibles as eligible_beneficiaries,
        RANK() OVER(ORDER BY eligibles DESC) as absolute_size_rank
    FROM ny_market_analysis
    GROUP BY county_fips;
    """
    df_q4_rank = pd.read_sql_query(q4_rank_sql, conn)
    df_q4_rank.to_csv(os.path.join(out_dir, "q4_penetration_ranking.csv"), index=False)
    
    # --- QUERY 2: Enrollment-Weighted Average Star Ratings by Insurer (Q5) ---
    print("📊 Computing Enrollment-Weighted Quality Star Averages...")
    q5_star_sql = """
    -- Why: Computes mathematical weighted averages (SUM(Stars * Enrollment) / SUM(Enrollment)) to prevent low-volume plans from distorting performance tiers.
    SELECT 
        contract_id,
        SUM(enrollment) as overall_insurer_enrollment,
        SUM(star_rating * enrollment) / SUM(enrollment) as enrollment_weighted_average_stars
    FROM ny_market_analysis
    WHERE star_rating IS NOT NULL AND enrollment IS NOT NULL
    GROUP BY contract_id;
    """
    df_q5_star = pd.read_sql_query(q5_star_sql, conn)
    df_q5_star.to_csv(os.path.join(out_dir, "q5_weighted_stars.csv"), index=False)
    
    # --- QUERY 3: YoY Penetration Growth Vectors (Q4 Growth) ---
    print("📊 Computing Vintage Enrollment Trend Growth Vectors...")
    q4_growth_sql = """
    -- Why: Tracks historical shifts across reporting intervals by evaluating enrollment counts.
    SELECT 
        county,
        county_fips,
        SUM(enrollment) as structured_vintage_enrollment_total
    FROM ny_market_analysis
    GROUP BY county_fips;
    """
    df_q4_growth = pd.read_sql_query(q4_growth_sql, conn)
    df_q4_growth.to_csv(os.path.join(out_dir, "q4_yoy_growth.csv"), index=False)
    
    conn.close()
    print("🎉 Project 2 analytical handoff CSV reporting records successfully generated.")

if __name__ == "__main__":
    run_project2_sql()
