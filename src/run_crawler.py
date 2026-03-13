from crawler.web_crawler import run_crawler
from config import REQUEST_TIMEOUT,MAX_PAGES


if __name__ == "__main__":
    run_crawler("https://proofwiki.org/m", REQUEST_TIMEOUT,MAX_PAGES)