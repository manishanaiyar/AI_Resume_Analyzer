import os
import time
from job_scraper import search_jobs  # Import the fixed function
from matcher import classify_resume # Import classify_resume from matcher.py

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    """Display the application banner."""
    print("=" * 42)
    print("           🚀 AI RESUME ANALYZER 🚀          ")
    print("=" * 42)
    print("\n✅ System Ready!\n")

def upload_resume():
    """Processes resume and predicts the job category using matcher.py."""
    print("\n📂 RESUME UPLOAD")
    print("-" * 42)
    print("Please ensure your resume is a PDF file in the same directory.")
    print("-" * 42)

    file_name = input("\n📝 Enter resume file name (e.g., my_resume.pdf): ").strip()
    
    if not file_name:
        print("⚠️ No file selected. Exiting...")
        exit()
    
    # Check if the file exists before attempting to classify
    if not os.path.exists(file_name):
        print(f"❌ Error: File '{file_name}' not found! Please ensure the file is in the correct directory.")
        exit()

    print(f"\n🔍 Analyzing Resume: {file_name}...")
    time.sleep(1.5)  # Simulate a brief processing time

    #  Call classify_resume from matcher.py
    job_category = classify_resume(file_name)

    if job_category is None:
        print("❌ Failed to classify resume. Exiting.")
        exit()

    print(f"\n📌 Job Category Identified: 🖥️ {job_category}")

    return job_category

def display_jobs(jobs):
    """Paginate and display job listings."""
    if not jobs:
        print("\n⚠️ No matching job listings found. Try modifying your resume or keywords.\n")
        return
    
    print("\n------------------------------------------")
    print("💼 JOB LISTINGS")
    print("------------------------------------------\n")

    for i in range(0, len(jobs), 10):
        for j, job in enumerate(jobs[i:i+10], 1):
            print(f"🔹 [{i+j}] {job.get('job_title', 'Not provided')}")
            print(f"   🏢 Employer  : {job.get('employer_name', 'Not provided')}")
            print(f"   📍 Location  : {job.get('location', 'Not provided')}")
            print(f"   💰 Salary    : {job.get('salary', 'Not listed')}")
            print(f"   🔗 Apply     : {job.get('job_apply_link', 'No link available')}\n")

        user_input = input("Press Enter to see more jobs or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print("\n👋 Exiting job search.\n")
            return

def main():
    clear_screen()
    display_banner()

    # Step 1: Resume Upload and Classification
    job_category = upload_resume()

    # Step 2: Fetch Job Listings
    print("\n🔎 Searching for relevant job openings...")
    # Add a small delay for better UX
    time.sleep(1) 
    jobs = search_jobs(job_category)

    # Step 3: Display Jobs
    display_jobs(jobs)

if __name__ == "__main__":
    main()
