import re
import pandas as pd
from pathlib import Path

SKILL_PATTERNS = {
    "SQL": r"\bsql\b",
    "Python": r"\bpython\b",
    "R": r"(?<!\w)r(?!\w)",
    "Excel": r"\bexcel\b",
    "Tableau": r"\btableau\b",
    "Power BI": r"\bpower\s*bi\b",
    "Pandas": r"\bpandas\b",
    "Spark": r"\bspark\b",
    "AWS": r"\baws\b|\bamazon web services\b",
}

def assign_role(title):
    if not isinstance(title, str):
        return "Other"

    t = title.lower()

    if "machine learning" in t or " ai " in f" {t} " or " ml " in f" {t} ":
        return "AI/ML"

    if "analyst" in t or "data" in t or "bi" in t:
        return "Analytics"

    if "sdet" in t or "quality assurance" in t or "qa" in t or "test" in t or "testing" in t:
        return "QA"

    if (
        "engineer" in t or
        "developer" in t or
        "backend" in t or
        "frontend" in t or
        "full stack" in t
    ):
        return "Engineering"

    return "Other"

def extract_skills(text):
    if not isinstance(text, str):
        return []
    lower = text.lower()

    found = []
    for skill, pattern in SKILL_PATTERNS.items():
        if re.search(pattern, lower):
            found.append(skill)

    return found

def main():
    df = pd.read_csv("data/processed/jobs_clean.csv")

    df["role_group"] = df["title"].apply(assign_role)

    combined = (
        df["title"].fillna("") + " " +
        df["tags"].fillna("") + " " +
        df["description"].fillna("")
    )

    df["skills"] = combined.apply(extract_skills).apply(lambda x: ", ".join(x))

    Path("data/processed").mkdir(parents=True, exist_ok=True)
    out_csv = "data/processed/jobs_enriched.csv"
    df.to_csv(out_csv, index=False)

    print("Saved:", out_csv)
    print("\nRole counts:")
    print(df["role_group"].value_counts())

    dummies = df["skills"].str.get_dummies(sep=", ")
    if dummies.shape[1] > 0:
        print("\nTop skills (overall):")
        print(dummies.sum().sort_values(ascending=False).head(10))
    else:
        print("\nNo skills detected (check tags/description).")

if __name__ == "__main__":
    main()