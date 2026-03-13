from crawler.web_crawler import run_crawler
from config import REQUEST_TIMEOUT


if __name__ == "__main__":
    run_crawler("https://proofwiki.org/", REQUEST_TIMEOUT)