import re

def extract_skills(text):
    skills_list = ['python', 'java', 'sql', 'machine learning', 'deep learning', 'nlp', 'excel', 'pandas', 'flask']
    found = []
    for skill in skills_list:
        if re.search(r'\b' + skill + r'\b', text.lower()):
            found.append(skill)
    return list(set(found))