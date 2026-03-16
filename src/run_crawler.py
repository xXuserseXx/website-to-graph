from crawler.web_crawler import run_crawler
from config import REQUEST_TIMEOUT,MAX_PAGES,OUTPUT_JSON_PATH


if __name__ == "__main__":
    run_crawler("https://proofwiki.org/", REQUEST_TIMEOUT,MAX_PAGES, OUTPUT_JSON_PATH)