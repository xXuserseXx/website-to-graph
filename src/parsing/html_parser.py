from bs4 import BeautifulSoup
from urllib.parse import urljoin

# this extract hrefs from a given html, only works for relative wiki URLs
def extract_urls(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    urls = set()

    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        if not href.startswith("/wiki/"): # this is specific to the wiki crawler for proof wiki, not relevant for other pages
            continue
        absolute_url = urljoin(base_url, href)
        urls.add(absolute_url)

    return urls