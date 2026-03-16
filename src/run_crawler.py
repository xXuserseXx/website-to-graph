from crawler.web_crawler import run_crawler
from graphing.create_graph import save_graph
from config import REQUEST_TIMEOUT,MAX_PAGES,OUTPUT_JSON_PATH


if __name__ == "__main__":
    run_crawler("https://proofwiki.org/m", REQUEST_TIMEOUT,MAX_PAGES, OUTPUT_JSON_PATH)