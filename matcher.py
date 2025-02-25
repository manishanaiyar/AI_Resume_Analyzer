import os
import pickle
import pdfplumber

# Load model and vectorizer
try:
    with open("resume_classifier.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    with open("label_encoder.pkl", "rb") as label_file:
        label_encoder = pickle.load(label_file)
    print("✅ Model, Vectorizer, and Label Encoder Loaded Successfully!")
except Exception as e:
    print(f"❌ Error loading model in matcher.py: {e}")
    exit()

# ✅ Define classify_resume() function
def classify_resume(resume_file):
    """Processes a resume PDF and predicts the job category."""
    if not os.path.exists(resume_file):
        print(f"❌ Error: File '{resume_file}' not found!")
        return None

    try:
        # Extract text from PDF
        with pdfplumber.open(resume_file) as pdf:
            resume_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

        # Convert text into features
        resume_vector = vectorizer.transform([resume_text])

        # Predict job category
        predicted_label_index = model.predict(resume_vector)[0]
        predicted_job_category = label_encoder.inverse_transform([predicted_label_index])[0]

        print(f"✅ Predicted Job Category: {predicted_job_category}")  

        # **Save predicted category to a file for `main.py`**
        with open("predicted_category.txt", "w") as file:
            file.write(predicted_job_category)

        return predicted_job_category

    except Exception as e:
        print(f"❌ Error processing resume: {e}")
        return None

# ✅ Automatically classify a resume if `matcher.py` is run directly
if __name__ == "__main__":
    resume_file = input("\n📂 Enter resume file name (PDF): ").strip()
    classify_resume(resume_file)
