import os
import sqlite3
import pandas as pd
import pytest

def test_medicare_table_constraints():
    db_path = "data/medicare.db"
    assert os.path.exists(db_path), "❌ Staged medicare tracking database missing!"
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM ny_market_analysis;", conn)
    conn.close()
    
    # Core Data Field Constraints & Validations
    assert df['county_fips'].notnull().all(), "❌ Integrity break: Missing county FIPS code strings found!"
    
    if 'star_rating' in df.columns and not df['star_rating'].dropna().empty:
        valid_stars = df['star_rating'].dropna().between(1.0, 5.0).all()
        assert valid_stars, "❌ Quality range exception: Star ratings found outside 1-5 boundary limits!"
        
    if 'penetration' in df.columns and not df['penetration'].dropna().empty:
        valid_pen = df['penetration'].dropna().between(0.0, 100.0).all()
        assert valid_pen, "❌ Market tracking anomaly: Penetration rates found outside 0-100% boundary limits!"
    
    print("✅ Project 2 Table Constraints Validated Successfully.")
