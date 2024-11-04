import requests
from bs4 import BeautifulSoup
from collections import deque
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 10  # Maximum number of threads


def extract_links(wiki_page_url: str) -> list:
    """
    Extracts all the valid internal Wikipedia links from a given page URL.
    """
    try:
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
    except Exception as e:
        print(f"Error retrieving links from {wiki_page_url}: {e}")
        return []


def find_path(source_url: str, target_url: str) -> Optional[list]:
    """
    Finds the shortest path from source to target Wikipedia page using BFS and multithreading.

    Arguments:
    source_url -- Starting Wikipedia page URL
    target_url -- Target Wikipedia page URL

    Returns:
    List of URLs representing the path from source to target, or None if no path found.
    """
    if source_url == target_url:
        return [source_url]

    queue = deque([[source_url]])
    visited = set([source_url])

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while queue:
            path = queue.popleft()
            current_page = path[-1]

            try:
                # Submit a request to fetch links using multithreading
                future_to_url = {executor.submit(extract_links, current_page): current_page}
                for future in as_completed(future_to_url):
                    links = future.result()

                    for link in links:
                        if link == target_url:
                            return path + [link]

                        if link not in visited:
                            visited.add(link)
                            queue.append(path + [link])
            except Exception as e:
                print(f"Error processing {current_page}: {e}")

    return None
