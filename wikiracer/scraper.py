import requests
from bs4 import BeautifulSoup
from collections import deque
from typing import Optional

def extract_links(wiki_page_url: str) -> list:
    """
    Extracts all the valid internal Wikipedia links from a given page URL.
    """
    response = requests.get(wiki_page_url)

    if response.status_code != 200:
        raise Exception(f"Failed to retrieve page: {wiki_page_url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        href = link.get('href')
        if href.startswith('/wiki/') and not href.startswith('/wiki/Special:') and ':' not in href:
            links.append(f"https://en.wikipedia.org{href}")

    return links


def find_path(source_url: str, target_url: str) -> Optional[list]:
    """
    Finds the shortest path from source to target Wikipedia page using BFS.

    Arguments:
    source_url -- Starting Wikipedia page URL
    target_url -- Target Wikipedia page URL

    Returns:
    List of URLs representing the path from source to target, or None if no path found.
    """
    if source_url == target_url:
        return [source_url]

    queue = deque([[source_url]])
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

                if link == target_url:
                    return new_path

                visited.add(link)
                queue.append(new_path)

    return None
