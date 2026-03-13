# This handles all the webcalls, and logic (already visited set, calling parser, calling graph builder)

from parsing.html_parser import extract_urls
from graphing.create_graph import create_node, add_edge

import requests

from collections import deque

def run_crawler(start_url: str, timeout: int, max_pages: int ):
    waiting = deque([start_url])

    seen = {start_url}
    visited = set()

    while waiting and len(visited) < max_pages:
        
        current_url = waiting.popleft()
            
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, timeout=timeout)
            response.raise_for_status
        except requests.exceptions.RequestException as e:
            print(f"Error while receiving html: {e}")

        urls = extract_urls(response.text, start_url)


        for url in urls:
            add_edge(current_url, url)
            

            if url in seen:
                continue
            print(f"Found new URL: {url}")
            create_node(url)
            seen.add(url)
            waiting.append(url)

        
    print(len(visited))



