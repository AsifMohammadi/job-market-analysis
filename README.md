Job Market Analysis (Web Data + SQL)

Overview

This project analyzes remote job postings to compare skill requirements across job roles, with a focus on Engineering and Analytics positions.

Data Source
Remote job postings collected from the Remote OK public job feed
Job URLs preserved for attribution

Tools
Python, pandas, SQLite, SQL, matplotlib, Jupyter Notebook

What I Did
Collected 99 remote job postings using a web API
Cleaned and structured the data into a SQLite database
Assigned jobs to role families (Engineering, Analytics, AI/ML, QA)
Used SQL to analyze skill demand by role
Created simple visualizations to compare roles

Key Findings
Engineering roles appeared most frequently.
Analytics roles emphasized SQL and Python.
Engineering roles showed higher demand for AWS.

How to Run
Install dependencies:
pip install -r requirements.txt

Run the data pipeline:
python src/collect.py
python src/transform.py
python src/enrich.py
python src/load_db.py

Open the analysis notebook:
notebooks/job_market_sql_analysis.ipynb

Run all cells to view SQL results and visualizations.

Data Source: Remote OK public job feed (job URLs preserved for attribution).