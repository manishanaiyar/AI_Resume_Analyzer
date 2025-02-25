import os
import time
from job_scraper import search_jobs  # Import the fixed function

def clear_screen():
    """Clear the terminal screen for better readability."""
    os.system("cls" if os.name == "nt" else "clear")

def display_banner():
    """Display the application banner."""
    print("=" * 42)
    print("         🚀 AI RESUME ANALYZER 🚀         ")
    print("=" * 42)
    print("\n✅ System Ready!\n")

def upload_resume():
    """Simulate resume upload (manual or file browsing)."""
    print("\n📂 RESUME UPLOAD")
    print("-" * 42)
    print("1️⃣  Enter the file name manually")
    print("2️⃣  Press [Enter] to browse files")
    print("-" * 42)

    file_name = input("\n📝 Enter resume file name (or press Enter to select): ").strip()
    
    if not file_name:
        print("⚠️ No file selected. Exiting...")
        exit()
    
    print("\n🔍 Analyzing Resume...")
    time.sleep(1.5)  # Simulate processing time

    # Simulate job category detection
    job_category = "INFORMATION TECHNOLOGY"
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

    # Step 1: Resume Upload
    job_category = upload_resume()

    # Step 2: Fetch Job Listings
    print("\n🔎 Searching for relevant job openings...")
    jobs = search_jobs(job_category)

    # Step 3: Display Jobs
    display_jobs(jobs)

if __name__ == "__main__":
    main()
