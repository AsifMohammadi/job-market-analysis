import json
from pathlib import Path
import pandas as pd

RAW_JSON_PATH = "data/raw/remoteok_jobs_latest.json"

def main():
    with open(RAW_JSON_PATH, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    rows = []
    for j in jobs:
        rows.append({
            "job_id": j.get("id"),
            "title": j.get("position"),
            "company_name": j.get("company"),
            "location": j.get("location"),
            "tags": ", ".join(j.get("tags", [])),
            "url": j.get("url"),
            "date": j.get("date"),
            "description": j.get("description", "")
        })

    df = pd.DataFrame(rows)

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    out_csv = "data/processed/jobs_clean.csv"
    df.to_csv(out_csv, index=False)

    print("Saved:", out_csv)
    print("Rows:", len(df))
    print(df[["job_id", "title", "company_name", "tags"]].head(3))

if __name__ == "__main__":
    main()
