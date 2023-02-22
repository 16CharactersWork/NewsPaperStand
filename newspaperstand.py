import os
import webbrowser
import time
import requests
from bs4 import BeautifulSoup

url = "https://freemagazines.top/newspapers"

session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Referer": url
}

response = session.get(url)
time.sleep(5)  # Add a delay to mimic human behavior

soup = BeautifulSoup(response.text, "html.parser")

# Find all links with a "bookmark" attribute and print their href and bookmark values
bookmarks = soup.find_all("a", attrs={"rel": "bookmark"})
for i, bookmark in enumerate(bookmarks):
    print(f"Bookmark {i+1}: {bookmark['href']}")

# Read links to ignore from a text file
ignore_links = set()
with open("ignore_links.txt", "r") as f:
    for line in f:
        ignore_links.add(line.strip())

# Prompt the user to select a bookmark to follow
bookmark_choice = None
while bookmark_choice is None:
    try:
        bookmark_choice = int(input("Enter the number of the bookmark you want to follow: "))
        if bookmark_choice < 1 or bookmark_choice > len(bookmarks):
            raise ValueError
        bookmark_links = soup.find_all("a", attrs={"rel": "bookmark"})
        bookmark_link = bookmark_links[bookmark_choice-1]
    except ValueError:
        print("Invalid input. Please enter a number between 1 and", len(bookmarks))
        continue

# Follow the selected bookmark and scrape links that start with "https://app.blackhole.run" or have a "Download PDF" button
pdf_links = set()
href = bookmark_link.get("href")
if href.startswith("https://freemagazines.top"):
    response = session.get(href)
    time.sleep(5)  # Add a delay to mimic human behavior
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = set(link.get("href") for link in soup.find_all("a") if link.get("href") and (link.get("href").startswith("https://app.blackhole.run") or link.find("button", text="Download PDF")))
else:
    pdf_links.add(href)

pdf_links -= ignore_links

# Open the selected PDF links in the default browser
if not pdf_links:
    print("No PDF links found.")
else:
    print("PDF links:")
    for i, link in enumerate(pdf_links):
        print(f"{i+1}. {link}")
    
    while True:
        try:
            link_choice = int(input("Enter the number of the link you want to open: "))
            if link_choice < 1 or link_choice > len(pdf_links):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and", len(pdf_links))

    webbrowser.open(list(pdf_links)[link_choice-1])
