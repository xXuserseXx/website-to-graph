from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    urls = set()

    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        if href.startswith("/wiki/"):
            absolute_url = urljoin(base_url, href)
            urls.add(absolute_url)

    return urls