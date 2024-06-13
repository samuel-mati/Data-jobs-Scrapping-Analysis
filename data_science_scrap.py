import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Base URL for job listings
base_url = "https://datajobs.com/Data-Science-Jobs~{}"

# Function to fetch job listings from a given page URL
def fetch_job_listings(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_divs = soup.find_all('div', style="margin-bottom:10px; padding-bottom:10px; border-bottom:#ddd dashed 1px;")

    job_list = []

    for job_div in job_divs:
        title_div = job_div.find('div', style="margin-left:13px; font-size:16px;")
        if title_div and title_div.a:
            job_title = title_div.a.text.strip()
            job_link = urljoin(base_url, title_div.a['href'])
            company = title_div.find('span', style="font-size:14px; text-transform:capitalize;").text.strip()
            location_div = job_div.find('div', style="margin-left:13px; font-size:12px;")
            location = location_div.find('span', style="font-size:14px; text-transform:capitalize;").text.strip() if location_div else "Unknown"

            job_list.append({
                'title': job_title,
                'company': company,
                'location': location,
                'link': job_link
            })
    
    return job_list, soup

# Function to fetch job descriptions from individual job pages
def fetch_job_description(job_url):
    response = requests.get(job_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    description_div = soup.find('div', class_='jobpost-table-cell-2')
    
    if description_div:
        return description_div.get_text(separator='\n').strip()
    else:
        return "Description not found"

# Initialize variables
current_page_num = 1
all_jobs = []

while current_page_num < 47:  # Assuming 47 pages
    current_page_url = base_url.format(current_page_num)
    job_list, soup = fetch_job_listings(current_page_url)
    all_jobs.extend(job_list)
    
    current_page_num += 1

# Create a DataFrame to store the job details
job_df = pd.DataFrame(all_jobs)

# Add descriptions to the DataFrame
job_df['description'] = job_df['link'].apply(fetch_job_description)

# Save the DataFrame to a CSV file
job_df.to_csv('data_jobs.csv', index=False)

print("Job details have been saved to data_science_jobs.csv")
