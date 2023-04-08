import os
import webbrowser
import time
import requests
import dialog
import sys
import json
from bs4 import BeautifulSoup


BOOKMARKS_FILE = "bookmarks.txt"


def read_bookmarks():
    if os.path.exists(BOOKMARKS_FILE):
        with open(BOOKMARKS_FILE, "r") as f:
            bookmarks = json.load(f)
    else:
        bookmarks = []
    return bookmarks


def write_bookmarks(bookmarks):
    with open(BOOKMARKS_FILE, "w") as f:
        json.dump(bookmarks, f)


def add_bookmark():
    d = dialog.Dialog()
    d.set_background_title("Add Bookmark")
    code, url = d.inputbox("Enter the URL of the article:")
    if code == d.OK and url.strip():
        response = requests.get(url.strip())
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title else url.strip()
            bookmarks = read_bookmarks()
            bookmarks.append({"url": url.strip(), "title": title})
            write_bookmarks(bookmarks)
            d.msgbox(f"Bookmark '{title}' added successfully.")
        else:
            d.msgbox(f"Error: {response.status_code}")
    else:
        sys.exit(0)


def get_article(bookmark_url):
    response = requests.get(bookmark_url)
    soup = BeautifulSoup(response.text, "html.parser")
    article = ""
    for p in soup.find_all("p"):
        article += p.text.strip() + "\n\n"
    return article


def display_article(article):
    d = dialog.Dialog()
    d.set_background_title("Article")
    d.msgbox(article)


def scrape_pdf_links(url, session):
    response = session.get(url)
    time.sleep(5)
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = set()
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if href and (href.startswith("https://app.blackhole.run") or link.find("button", string="Download PDF")):
            pdf_links.add(href)
    return pdf_links


def main():
    if not os.path.exists(BOOKMARKS_FILE):
        write_bookmarks([])

    d = dialog.Dialog(dialog="dialog")
    bookmarks = read_bookmarks()
    bookmark_choices = [(bookmark["url"], bookmark["title"], False) for bookmark in bookmarks]
    bookmark_choices.append(("Add Bookmark", "Add Bookmark", True))
    code, bookmark_choice = d.radiolist("Choose a newspaper to view:", choices=bookmark_choices)
    if code == d.OK:
        if bookmark_choice == "Add Bookmark":
            add_bookmark()
        else:
            bookmark_url = bookmark_choice
            article = get_article(bookmark_url)
            display_article(article)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
