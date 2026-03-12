# This handles all the webcalls, and logic (already visited set, calling parser, calling graph builder)

from parsing.html_parser import extract_url
from graphing.create_graph import create_node, add_edge
import queue
import requests

def run_crawler(start_url: str, timeout: int):
    waiting = queue.Queue()
    waiting.put(start_url)

    seen = {start_url}
    visited = set()

    while not waiting.empty():
        try:
            current_url = waiting.get()
            
            if current_url not in visited:
                visited.add(current_url)
                create_node(current_url)

            response = requests.get(current_url, timeout=timeout)
            urls = extract_url(response.text)


            for url in urls:
                add_edge(current_url, url)
                if url not in seen:
                    waiting.put(url)
                    seen.add(url)

                    create_node(url)

        except requests.exceptions.RequestException as e:
            print(f"Request Failes! {e}")




