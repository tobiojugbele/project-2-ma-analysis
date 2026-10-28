import os
import zipfile
import pandas as pd
import numpy as np

def run_medicare_etl():
    print("🚀 Project 2 ETL: Processing Medicare Advantage data clusters...")
    raw_dir = "data/raw"
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    # 1. Process Star Ratings Archive
    star_zip = os.path.join(raw_dir, "2027-star-ratings-data-tables-oct-8-2026.zip")
    if os.path.exists(star_zip):
        print("📦 Processing Star Ratings Data Table from archive...")
        with zipfile.ZipFile(star_zip, "r") as z:
            xlsx_files = [f for f in z.namelist() if f.endswith(".xlsx") and not f.startswith("._")]
            if xlsx_files:
                with z.open(xlsx_files[0]) as f:
                    df_star = pd.read_excel(f, engine="openpyxl")
                df_star.columns = df_star.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
                df_star.to_csv(os.path.join(output_dir, "star_ratings_cleaned.csv"), index=False)
                print(f"✅ Cleaned Star Ratings shape: {df_star.shape}")
    else:
        print("⚠️ Warning: Star Ratings zip file archive not found in data/raw/")

    # 2. Process and Filter Other Available Raw Data Files for New York
    for file in os.listdir(raw_dir):
        if file.startswith("._") or file.startswith(".DS_Store") or file.endswith(".zip"):
            continue
        fp = os.path.join(raw_dir, file)
        if file.endswith(".csv") or file.endswith(".xlsx"):
            print(f"📦 Filtering and cleaning data file: {file}...")
            if file.endswith(".csv"):
                df = pd.read_csv(fp, low_memory=False)
            else:
                df = pd.read_excel(fp, engine="openpyxl")
            df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

            state_cols = [c for c in df.columns if "state" in c]
            if state_cols:
                sc = state_cols[0]
                df = df[df[sc].astype(str).str.upper().str.contains("NY|NEW YORK", regex=True)]

            enroll_cols = [c for c in df.columns if "enrollment" in c or "members" in c]
            for ec in enroll_cols:
                df[ec] = pd.to_numeric(df[ec].astype(str).str.replace(",", ""), errors="coerce")
                df.loc[df[ec] < 11, ec] = np.nan

            fips_cols = [c for c in df.columns if "fips" in c or "county_code" in c]
            for fc in fips_cols:
                df[fc] = df[fc].astype(str).str.split(".").str.str[0].str.zfill(5)

            county_cols = [c for c in df.columns if "county" in c and "code" not in c]
            for cc in county_cols:
                df[cc] = df[cc].astype(str).str.strip().str.upper()

            out_name = file.split(".")[0] + "_cleaned.csv"
            df.to_csv(os.path.join(output_dir, out_name), index=False)
            print(f"✅ Exported clean NY records framework for {file}: {df.shape}")

    print("🎉 Project 2 ETL tool step completed successfully.")

if __name__ == "__main__":
    run_medicare_etl()
