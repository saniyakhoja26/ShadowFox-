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

print("Content extracted from ShadowFox website:\n")

# Display extracted text
for i, para in enumerate(paragraphs, start=1):
    text = para.text.strip()
    if text:  # avoid empty lines
        print(f"{i}. {text}")