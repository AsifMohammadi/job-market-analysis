import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/jobs.db"
CSV_PATH = "data/processed/jobs_enriched.csv"

def main():
    Path("data").mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_csv(CSV_PATH)

    # 1) jobs table
    df.to_sql("jobs", conn, if_exists="replace", index=False)

    # 2) skills table + job_skills table
    conn.execute("DROP TABLE IF EXISTS skills")
    conn.execute("DROP TABLE IF EXISTS job_skills")

    conn.execute("""
        CREATE TABLE skills (
            skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_name TEXT UNIQUE NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE job_skills (
            job_id INTEGER NOT NULL,
            skill_id INTEGER NOT NULL,
            PRIMARY KEY (job_id, skill_id)
        )
    """)

    # Unique skills set
    all_skills = set()
    for s in df["skills"].fillna(""):
        for skill in s.split(", "):
            if skill:
                all_skills.add(skill)

    # Insert skills
    for skill in sorted(all_skills):
        conn.execute("INSERT OR IGNORE INTO skills (skill_name) VALUES (?)", (skill,))

    # Map skill_name -> skill_id
    skill_map = {
        name: sid
        for sid, name in conn.execute("SELECT skill_id, skill_name FROM skills").fetchall()
    }

    # Insert job-skill links
    links = []
    for _, row in df.iterrows():
        job_id = int(row["job_id"])
        skills = row["skills"] if isinstance(row["skills"], str) else ""
        for skill in skills.split(", "):
            if skill:
                links.append((job_id, skill_map[skill]))

    conn.executemany(
        "INSERT OR IGNORE INTO job_skills (job_id, skill_id) VALUES (?, ?)",
        links
    )

    conn.commit()
    conn.close()

    print("Database created:", DB_PATH)
    print("Jobs:", len(df))
    print("Unique skills:", len(all_skills))
    print("Job-skill links:", len(links))

if __name__ == "__main__":
    main()
