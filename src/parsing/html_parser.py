from urllib.parse import urldefrag, urljoin, urlparse

from bs4 import BeautifulSoup


def _normalize_url(url: str) -> str:
    normalized_url, _ = urldefrag(url)
    parsed = urlparse(normalized_url)

    path = parsed.path.rstrip("/") or "/"
    return parsed._replace(path=path).geturl()


def extract_urls(html_content: str, base_url: str, allowed_domain: str):
    soup = BeautifulSoup(html_content, "html.parser")
    urls = set()

    for tag in soup.find_all("a"):
        href = tag.get("href")

        if not href:
            continue

        absolute_url = urljoin(base_url, href)
        parsed = urlparse(absolute_url)

        if parsed.netloc != allowed_domain:
            continue

        if not parsed.path.startswith("/wiki/"):
            continue

        urls.add(_normalize_url(absolute_url))

    return urls
