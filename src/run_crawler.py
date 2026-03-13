from config import MAX_DEPTH, MAX_PAGES, REQUEST_TIMEOUT
from crawler.web_crawler import run_crawler


if __name__ == "__main__":
    run_crawler(
        start_url="https://proofwiki.org/",
        timeout=REQUEST_TIMEOUT,
        max_pages=MAX_PAGES,
        max_depth=MAX_DEPTH,
    )
