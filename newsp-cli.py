import os
import requests
from bs4 import BeautifulSoup
import time
import webbrowser

url = "https://freemagazines.top/newspapers"

session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Referer": url
}

response = session.get(url)
time.sleep(5)  # Add a delay to mimic human behavior

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href.startswith("http"):
        href = href.replace("blackhole.run", "app.blackhole.run")
        links.append(href)

print("Select a link:")
for i, link in enumerate(links):
    print(f"{i+1}. {link}")

selected_link = None
while selected_link is None:
    try:
        choice = int(input("Enter the number of the link you want to select: "))
        if 1 <= choice <= len(links):
            selected_link = links[choice-1]
        else:
            print("Invalid choice. Please enter a number between 1 and", len(links))
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Selected link:", selected_link)

response = session.get(selected_link)
time.sleep(5)  # Add a delay to mimic human behavior

soup = BeautifulSoup(response.text, "html.parser")

pdf_links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.startswith("https://app.blackhole.run"):
        pdf_links.append(href)

if not pdf_links:
    print("No PDF links found.")
else:
    print("PDF links:")
    for i, link in enumerate(pdf_links):
        print(f"{i+1}. {link}")
    
    download_choice = input("Do you want to download a PDF file? (y/n) ")
    if download_choice.lower() == "y":
        pdf_choice = None
        while pdf_choice is None:
            try:
                pdf_choice = int(input("Enter the number of the PDF you want to download: "))
                if 1 <= pdf_choice <= len(pdf_links):
                    pdf_url = pdf_links[pdf_choice-1]
                    response = session.get(pdf_url)
                    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
                    filename = os.path.basename(pdf_url)
                    file_path = os.path.join(downloads_folder, filename)
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print("Downloaded file:", file_path)
                    webbrowser.open(pdf_url)
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(pdf_links))
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("PDF download cancelled.")
