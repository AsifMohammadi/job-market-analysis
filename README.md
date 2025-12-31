# Job Market Analysis (Web Data + SQL)

## Overview
This project analyzes remote job postings to compare **skill requirements across job roles**, with a focus on **Engineering** and **Analytics** positions.

---

## Data Source
- Remote job postings from the **Remote OK public job feed**
- Job URLs preserved for attribution

---

## Tools Used
- Python  
- pandas  
- SQLite  
- SQL  
- matplotlib  
- Jupyter Notebook  

---

## What I Did
- Collected **99 remote job postings** using a web API  
- Cleaned and structured the data into a **SQLite database**  
- Grouped jobs into role families (Engineering, Analytics, AI/ML, QA)  
- Used **SQL joins and aggregations** to analyze skill demand  
- Created **simple bar charts** to visualize results  

---

## Key Findings
- Engineering roles appeared most frequently.
- Analytics roles emphasized **SQL** and **Python**.
- Engineering roles showed stronger demand for **AWS**.
- Some roles required both SQL and Python.

---

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the data pipeline:
   ```bash
   python src/collect.py
   python src/transform.py
   python src/enrich.py
   python src/load_db.py

4. Open the analysis notebook:
   ```bash
   notebooks/job_market_sql_analysis.ipynb

Run all cells to view SQL results and visualizations.

Data Source: Remote OK public job feed (job URLs preserved for attribution).
