PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS job_skills;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
  job_id INTEGER PRIMARY KEY,
  source TEXT NOT NULL,
  title TEXT,
  company_name TEXT,
  category TEXT,
  job_type TEXT,
  publication_date TEXT,
  candidate_required_location TEXT,
  salary_raw TEXT,
  url TEXT UNIQUE,
  description_html TEXT
);

CREATE TABLE skills (
  skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
  skill_name TEXT UNIQUE NOT NULL
);

CREATE TABLE job_skills (
  job_id INTEGER NOT NULL,
  skill_id INTEGER NOT NULL,
  PRIMARY KEY (job_id, skill_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id) ON DELETE CASCADE,
  FOREIGN KEY (skill_id) REFERENCES skills(skill_id) ON DELETE CASCADE
);