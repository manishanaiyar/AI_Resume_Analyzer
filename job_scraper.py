import requests

def search_jobs(job_category, num_pages=3):
    """Fetch job listings from API and return a list of job dictionaries."""
    
    if not job_category:
        print("❌ Error: Job category is empty!")
        return []

    print(f"🔍 Searching jobs for category: {job_category}")

    # API credentials
    API_KEY = "f37b91374emsheea622572c606bap18a0c0jsn8675c4573498"
    API_URL = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    all_jobs = []

    for page in range(1, num_pages + 1):
        params = {"query": job_category, "page": page}  # Removed `num_pages`
        
        try:
            response = requests.get(API_URL, headers=headers, params=params)

            if response.status_code == 200:
                job_data = response.json()
                jobs = job_data.get("data", [])

                if not jobs:
                    print(f"⚠️ No jobs found on page {page}. Stopping search.")
                    break
                
                all_jobs.extend(jobs)
            else:
                print(f"❌ API Request Failed! Status Code: {response.status_code}")
                print("🔍 Response:", response.text)
                return []  # Ensure it returns an empty list instead of None
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: Unable to fetch job listings. Exception: {e}")
            return []  # Ensure it returns an empty list instead of None
    
    if not all_jobs:
        print("\n⚠️ No matching job listings found. Try modifying your resume or keywords.\n")
        return []

    return all_jobs  # ✅ Always returns a list, even if empty
