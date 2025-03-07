import requests 
#import pandas as pd

# define the api url 
API_URL = "https://clinicaltrials.gov/api/v2/studies"

# example 
#https://clinicaltrials.gov/api/v2/studies?
# filter.overallStatus=COMPLETED
# &aggFilters=phase:2
# &filter.advanced=AREA[PrimaryCompletionDate]RANGE[2025-01-01,%20MAX]
# &query.cond=colorectal%20cancer

def fetch_clinical_trials(
        phase = ["2"],
        status = ["COMPLETED", "TERMINATED"],
        primary_completion_from = "2023-08-29",
        primary_completion_to = "2023-09-03",
        conditions = ["lung cancer"] 
):
    
    params = {
        "filter.overallStatus": ",".join(status),
        "aggFilters": f"phase:{','.join(phase)}",  # Uses aggFilters for Phase 2
        "filter.advanced": f"AREA[PrimaryCompletionDate]RANGE[{primary_completion_from}, {primary_completion_to}]",  # Uses Essie syntax for date filtering
        "query.cond": ",".join(conditions),  # Uses query.cond for disease filtering
        "fields" : "NCTId,InterventionType,OfficialTitle,Phase,OverallStatus,PrimaryCompletionDate" , # relevant fields for data collection 
        "pageSize": 100,
    }

    # debug url 
    query_string = "&".join(f"{key}={value}" for key, value in params.items())
    full_url = f"{API_URL}?{query_string}"
    print("Full API Request URL:", full_url)

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raises an error for non-200 responses
    except requests.exceptions.RequestException as e:
        print("API Request Failed:", e)
        response = None  # Set to None if request fails

    if response:
        data = response.json()
        #print(data)  # View the full JSON response

fetch_clinical_trials()


#https://clinicaltrials.gov/api/v2/studies?filter.overallStatus=COMPLETED&aggFilters=phase:2&filter.advanced=AREA[PrimaryCompletionDate]RANGE[2025-01-01,%20MAX]&query.cond=colorectal%20cancer