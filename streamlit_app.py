import streamlit as st
from utils.parser import extract_skills
from utils.recommender import recommend_jobs

def main():
    st.set_page_config(page_title="Resume Analyzer & Job Recommender", layout="centered")
    st.title("📄 Resume Analyzer & Job Recommender")
    st.write("Upload your resume and get top job role suggestions based on your skills.")

    uploaded_file = st.file_uploader("Upload Resume (.txt only)", type=["txt"])

    if uploaded_file is not None:
        resume_text = uploaded_file.read().decode("utf-8")
        st.subheader("✅ Extracted Resume Text")
        st.code(resume_text)

        skills = extract_skills(resume_text)
        st.subheader("🧠 Extracted Skills")
        st.write(skills)

        recommendations = recommend_jobs(resume_text)

        if not recommendations.empty:
            st.subheader("🎯 Recommended Job Roles")
            for _, row in recommendations.iterrows():
                st.markdown(f"🔹 **{row['title']}** — Similarity: `{row['similarity']:.2f}`")
        else:
            st.warning("No matching jobs found.")

if __name__ == "__main__":
    main()