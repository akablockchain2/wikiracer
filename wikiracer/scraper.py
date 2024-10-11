# wikiracer/scraper.py

import requests
from bs4 import BeautifulSoup
from collections import deque

WIKI_URL = "https://en.wikipedia.org"


def extract_links(wiki_page: str) -> list:
    """
    Extracts all the valid internal Wikipedia links from a given page.
    """
    url = f"{WIKI_URL}/wiki/{wiki_page}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page: {wiki_page}")

    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href.startswith('/wiki/') and not href.startswith('/wiki/Special:') and ':' not in href:
            links.append(href.split("/wiki/")[-1])

    return links


def find_path(source: str, target: str) -> list:
    """
    Finds the shortest path from source to target Wikipedia page using BFS.

    Arguments:
    source -- Starting Wikipedia page
    target -- Target Wikipedia page

    Returns:
    List of pages representing the path from source to target, or None if no path found.
    """
    if source == target:
        return [source]

    queue = deque([[source]])
    visited = set()

    while queue:
        path = queue.popleft()
        current_page = path[-1]

        try:
            links = extract_links(current_page)
        except Exception as e:
            print(f"Error extracting links from {current_page}: {e}")
            continue

        for link in links:
            if link not in visited:
                new_path = list(path)
                new_path.append(link)

                if link == target:
                    return new_path

                visited.add(link)
                queue.append(new_path)

    return None
