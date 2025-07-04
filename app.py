from utils.parser import extract_skills
from utils.recommender import recommend_jobs

def main():
    # Read resume text
    with open("resumes/sample_resume.txt", "r") as f:
        resume_text = f.read()

    # Extract skills
    skills = extract_skills(resume_text)
    print("✅ Extracted Skills:", skills)

    recommendations = recommend_jobs(resume_text)
    
    print("\n🧪 Raw Recommendations Data:")
    print(recommendations)  # <-- Add this line to see if data is returned

    # Optional: print more nicely
    if not recommendations.empty:
        print("\n🎯 Top Job Recommendations:")
        for i, row in recommendations.iterrows():
            print(f"🔹 {row['title']} - Similarity Score: {row['similarity']:.2f}")
    else:
        print("⚠️ No recommendations found.")

if __name__ == "__main__":
    main()