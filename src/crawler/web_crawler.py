# This handles all the webcalls, and logic (already visited set, calling parser, calling graph builder)

from collections import deque
from urllib.parse import urlparse

import requests

from graphing.create_graph import add_edge, create_node
from parsing.html_parser import extract_urls


def run_crawler(start_url: str, timeout: int, max_pages: int, max_depth: int):
    waiting = deque([(start_url, 0)])

    allowed_domain = urlparse(start_url).netloc

    seen = {start_url}
    visited = set()

    while waiting and len(visited) < max_pages:
        current_url, depth = waiting.popleft()

        if current_url in visited:
            continue

        visited.add(current_url)
        create_node(current_url)

        if depth >= max_depth:
            continue

        try:
            response = requests.get(current_url, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {current_url}: {e}")
            continue

        content_type = response.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            continue

        urls = extract_urls(response.text, current_url, allowed_domain)

        for url in urls:
            add_edge(current_url, url)
            create_node(url)

            if url in seen or len(seen) >= max_pages:
                continue

            seen.add(url)
            waiting.append((url, depth + 1))

    print(f"Visited pages: {len(visited)}")
