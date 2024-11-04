# Wikiracer
Wikiracer is a command-line tool that finds the shortest path between two Wikipedia pages using a breadth-first search (BFS) algorithm. It allows you to see the sequence of links required to navigate from one Wikipedia page to another, showcasing the interconnected nature of the Wikipedia graph.

## Features
- Accepts two Wikipedia pages as input: `source` and `target`.
- Finds the shortest path between the pages using BFS.
- Outputs the sequence of pages from `source` to `target` if a path is found.
- Displays a message if no path exists between the given pages.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/akablockchain2/wikiracer.git  
   cd wikiracer
   ```
2. Create and activate a virtual environment:  
   ```bash
    python3 -m venv .venv  
    source .venv/bin/activate
   ```
3. Install the dependencies:  
   `pip3 install -r requirements.txt`
4. Install the project in editable mode:  
   `pip3 install -e .`

## Usage
The tool accepts two arguments: the `source` page and the `target` page. Use the CLI as follows:
```bash
wikiracer "Python_(programming_language)" "Java_virtual_machine"
```

### Example Output
If a path is found between the source and target pages, the output will look like this:  
Python_(programming_language) -> Computer_science -> Artificial_intelligence  
If no path is found, the output will be:  
No path found from Python_(programming_language) to Artificial_intelligence.

### Command-line Arguments
- `source` - The starting Wikipedia page. It should be the exact page name used in the URL (e.g., Python_(programming_language)).
- `target` - The target Wikipedia page you want to reach.

### Additional Examples
```bash
wikiracer "Albert_Einstein" "Theory_of_relativity"  
wikiracer "New_York_City" "Central_Park"
```

## Project Structure
The project structure is as follows:
```bash
wikiracer/  
├── wikiracer/  
│   ├── \_\_init\_\_.py  
│   ├── cli.py          # CLI entry point  
│   └── scraper.py      # Logic for extracting links and BFS algorithm  
├── .venv/              # Virtual environment  
├── setup.py            # Setup script for project installation  
├── requirements.txt    # Project dependencies  
└── README.md           # Project documentation  
```
## How It Works
1. The `cli.py` file serves as the command-line entry point. It accepts the `source` and `target` arguments.  
2. The `scraper.py` file contains the logic for extracting links from a Wikipedia page using `requests` and `BeautifulSoup`.  
3. The `find_path` function in `scraper.py` implements the BFS algorithm to find the shortest path between the `source` and `target` pages.

## Dependencies
- `requests` - For making HTTP requests to Wikipedia pages.  
- `beautifulsoup4` - For parsing HTML and extracting links from Wikipedia pages.  
- `click` - For building the command-line interface.
