import spacy
from spacy.matcher import PhraseMatcher

# ✅ Use a lightweight blank English pipeline — no model download needed
nlp = spacy.blank("en")

# 🔧 Define skill list
SKILLS = [
    "python", "java", "selenium", "selenium webdriver", "testng", "appium",
    "flask", "django", "sql", "pandas", "machine learning", "rest api"
]

# 🔍 Setup PhraseMatcher for exact/variant skill detection
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS]
matcher.add("SKILLS", patterns)

# 🧠 Skill extraction function
def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    found_skills = list(set([doc[start:end].text.lower() for _, start, end in matches]))
    return sorted(found_skills)
