"""
Task Level: Intermediate
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Web Scraper using BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup


# ShadowFox website URL
url = "https://shadowfox.in/"

try:
    # Send request to the website
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        print("ShadowFox website accessed successfully\n")
    else:
        print("Failed to access ShadowFox website")
        exit()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all paragraph text from the website
    paragraphs = soup.find_all("p")

    scraped_data = []

    # writing data into list
    for para in paragraphs:
        text = para.text.strip()
        if text:
            scraped_data.append(text)

    # save data to file
    with open("Web_Scraper_data.txt", "w", encoding="utf-8") as file:
        for line in scraped_data:
            file.write(line + "\n\n")

    print("✅ Data successfully scraped and saved to Web_Scraper_data.txt")

except Exception as e:
    print("❌ An error occurred during scraping:", e)
