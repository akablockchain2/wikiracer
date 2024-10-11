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

    # Извлекаем все ссылки со страницы
    for link in soup.find_all('a', href=True):
        href = link.get('href')
        # Фильтруем ссылки, чтобы исключить ссылки на страницы с символом '#' и внешние ресурсы
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

    # Очередь для BFS поиска: хранит пути в формате [source, page1, page2, ..., target]
    queue = deque([[source]])
    visited = set()  # Отслеживает посещенные страницы

    while queue:
        # Извлекаем текущий путь из очереди
        path = queue.popleft()
        current_page = path[-1]

        # Извлекаем все ссылки с текущей страницы
        try:
            links = extract_links(current_page)
        except Exception as e:
            print(f"Error extracting links from {current_page}: {e}")
            continue

        for link in links:
            if link not in visited:
                # Создаем новый путь, добавляя новую ссылку
                new_path = list(path)
                new_path.append(link)

                # Если нашли целевую страницу, возвращаем путь
                if link == target:
                    return new_path

                # Добавляем ссылку в посещенные и в очередь
                visited.add(link)
                queue.append(new_path)

    return None  # Путь не найден
