import spacy
from spacy.matcher import PhraseMatcher

# Load English NLP model
import spacy
from spacy.cli import download

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


# Define known skills (you can expand this list)
SKILLS = [
    "python", "java", "selenium", "selenium webdriver", "testng", "appium",
    "django", "flask", "sql", "pandas", "machine learning"
]

# Initialize matcher with lowercase matching
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill) for skill in SKILLS]
matcher.add("SKILLS", None, *patterns)

def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)
    found_skills = list(set([doc[start:end].text.lower() for _, start, end in matches]))
    return sorted(found_skills)
