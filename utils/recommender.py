import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def recommend_jobs(resume_text, job_data_path='jobs/jobs.csv', model_path='model/tfidf_vectorizer.pkl'):
    jobs_df = pd.read_csv(job_data_path)
    job_texts = jobs_df['description'].tolist()
    texts = [resume_text] + job_texts

    # ✅ Ensure model folder exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    if os.path.exists(model_path):
        vectorizer = joblib.load(model_path)
        vectors = vectorizer.transform(texts)
    else:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(texts)
        joblib.dump(vectorizer, model_path)

    resume_vec = vectors[0]
    job_vecs = vectors[1:]
    scores = cosine_similarity(resume_vec, job_vecs).flatten()

    jobs_df['similarity'] = scores
    top_matches = jobs_df.sort_values(by='similarity', ascending=False).head(3)
    return top_matches[['title', 'similarity']]