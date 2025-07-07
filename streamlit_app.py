import streamlit as st
from utils.parser import extract_skills
from utils.recommender import recommend_jobs
import docx  # NEW

def read_docx(file):
    doc = docx.Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

def main():
    st.set_page_config(page_title="Resume Analyzer", layout="centered")
    st.title("📄 Resume Analyzer & Job Recommender")

    uploaded_file = st.file_uploader("Upload Resume (.txt or .docx)", type=["txt", "docx"])
    
if uploaded_file is not None:
    if uploaded_file.name.endswith(".txt"):
        resume_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".docx"):
        resume_text = read_docx(uploaded_file)
    else:
        st.warning("Please upload a .txt or .docx file only.")

    st.subheader("✅ Resume Text")
    st.code(resume_text)

    with st.spinner("Extracting skills and finding jobs..."):
        skills = extract_skills(resume_text)
        results = recommend_jobs(resume_text)

    st.subheader("🧠 Extracted Skills")
    st.write(skills)

    st.subheader("🎯 Recommended Jobs")
    for _, row in results.iterrows():
        st.markdown(f"🔹 **{row['title']}** — Similarity: `{row['similarity']:.2f}`")


if __name__ == "__main__":
    main()
