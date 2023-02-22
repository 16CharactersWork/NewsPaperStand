import os
import webbrowser
import time
import requests
from bs4 import BeautifulSoup
import subprocess

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
for bookmark in bookmarks:
    print(f"Bookmark {bookmark['bookmark']}: {bookmark['href']}")

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
        bookmark_links = soup.find_all("a", attrs={"bookmark": str(bookmark_choice)})
        if not bookmark_links:
            print("No links found for bookmark", bookmark_choice)
            bookmark_choice = None
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

# Follow the selected bookmark and scrape links that start with "https://app.blackhole.run" or have a "Download PDF" button
pdf_links = set()
for link in bookmark_links:
    href = link.get("href")
    if href and href.startswith("https://app.blackhole.run") and href not in ignore_links:
        pdf_links.add(href)
    elif link.find("button", text="Download PDF"):
        button_href = link.get("href")
        if button_href and button_href.startswith("https://app.blackhole.run") and button_href not in ignore_links:
            pdf_links.add(button_href)

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

    # Open the PDF link in the default web browser on Linux
    subprocess.call(["xdg-open", pdf_links[link_choice-1]])
