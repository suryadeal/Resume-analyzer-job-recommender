import spacy
from spacy.matcher import PhraseMatcher

# Load English NLP model
import spacy
from spacy.cli import download
import streamlit as st

@st.cache_resource
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("⚠️ spaCy model not found. Downloading...")
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()
try:
    nlp = spacy.load("en")
except OSError:
    download("en")
    nlp = spacy.load("en")


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
