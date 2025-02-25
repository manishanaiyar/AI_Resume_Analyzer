import joblib

# Assuming you already trained 'best_rf' and 'vectorizer' in Google Colab
# Save the trained model
joblib.dump(best_rf, "resume_classifier.pkl")

# Save the TF-IDF vectorizer
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("✅ Model and vectorizer saved successfully!")
