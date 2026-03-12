# This scans loaded html files for href tags, and extracts the links for the subpages
# Using bs4 library

from utils.url_utils import clean_url
from bs4 import BeautifulSoup

def extract_url(html):
    pass