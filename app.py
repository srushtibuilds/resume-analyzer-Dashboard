import pandas as pd

# ---------- FILE PATHS ----------
SKILLS_PATH = "dataset/skills.csv"
RESUME_PATH = "dataset/resumes/resume1.txt"
JD_PATH = "dataset/job_descriptions/jd1.txt"

# ---------- READ SKILLS ----------
skills_df = pd.read_csv(SKILLS_PATH)
skills_list = skills_df["Skill"].str.lower().tolist()

# ---------- READ RESUME ----------
with open(RESUME_PATH, "r", encoding="utf-8") as f:
    resume_text = f.read().lower()

# ---------- READ JOB DESCRIPTION ----------
with open(JD_PATH, "r", encoding="utf-8") as f:
    jd_text = f.read().lower()

# ---------- SKILL MATCHING ----------
resume_skills = []
jd_skills = []

for skill in skills_list:
    if skill in resume_text:
        resume_skills.append(skill)
    if skill in jd_text:
        jd_skills.append(skill)

# ---------- MATCH PERCENTAGE ----------
matched_skills = set(resume_skills).intersection(set(jd_skills))

if len(jd_skills) > 0:
    match_percentage = (len(matched_skills) / len(jd_skills)) * 100
else:
    match_percentage = 0

# ---------- OUTPUT ----------
print("Skills in Resume:", resume_skills)
print("Skills in Job Description:", jd_skills)
print("Matched Skills:", list(matched_skills))
print(f"Match Percentage: {match_percentage:.2f}%")
