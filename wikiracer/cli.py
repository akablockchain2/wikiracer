# wikiracer/cli.py

import click
from wikiracer.scraper import find_path


@click.command()
@click.argument('source')
@click.argument('target')
def main(source, target):
    """
    Find the shortest path from source to target Wikipedia page using BFS.

    Arguments:
    source -- Starting Wikipedia page (e.g., "Python_(programming_language)")
    target -- Target Wikipedia page to reach (e.g., "Artificial_intelligence")
    """
    try:
        path = find_path(source, target)
        if path:
            print(" -> ".join(path))
        else:
            print(f"No path found from {source} to {target}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
