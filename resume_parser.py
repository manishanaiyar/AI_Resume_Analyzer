import os
import tkinter as tk
from tkinter import filedialog
import pdfplumber

def upload_resume():
    print("\n📂 How would you like to upload your resume?")
    print("1️⃣ Enter file path manually")
    print("2️⃣ Browse and upload (Recommended)")

    choice = input("\n🔹 Choose an option (1 or 2): ").strip()

    if choice == "1":
        resume_path = input("\n📂 Enter the full path of your resume (PDF): ").strip()
    elif choice == "2":
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window
        resume_path = filedialog.askopenfilename(title="Select Your Resume (PDF)", filetypes=[("PDF Files", "*.pdf")])
    else:
        print("❌ Invalid option. Please enter 1 or 2.")
        return None

    # Check if the file exists
    if not resume_path or not os.path.isfile(resume_path):
        print("❌ File not found! Please check the path and try again.")
        return None

    print(f"\n✅ Resume uploaded successfully: {resume_path}")
    return resume_path  # Return the file path for further processing

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

# Upload Resume
resume_file = upload_resume()

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    print("\n📜 Extracted Resume Text:\n", resume_text)
