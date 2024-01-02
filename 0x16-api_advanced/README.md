![Header Image](WIxXad8.png)
# Reddit API Advanced Project


## Overview

This project offers a set of Python scripts to interact with the Reddit API, allowing users to retrieve information about subreddits, fetch titles of hot articles, and count occurrences of specified keywords in these articles.

## Project Structure

- **`0-subs.py`**: Fetches the number of subscribers for a given subreddit.
- **`1-top_ten.py`**: Retrieves and prints titles of the first 10 hot posts from a specified subreddit.
- **`2-recurse.py`**: Recursively fetches all hot posts from a given subreddit and returns their titles.
- **`100-count.py`**: Recursively fetches hot posts and counts occurrences of specified keywords in their titles.

## Setup & Usage

### Prerequisites

- Python 3.x
- `requests` library

Install the required library using:

```bash
pip install requests
```

### Instructions
1. Navigate to the project directory.
2. Run the desired script using Python.

Examples:
* To fetch the number of subscribers for the `programming` subreddit:

```
python3 0-subs.py programming
```
To retrieve titles of the first 10 hot posts from the `programming` subreddit:
```
python3 1-top_ten.py programming
```
To recursively fetch all hot posts from the `programming` subreddit and count occurrences of keywords like `python`, `java`, and `javascript`:
```
python3 100-count.py programming "python java javascript"
```

### Notes
* Ensure that the subreddit name is valid; otherwise, the scripts might not produce the desired results.
* The Reddit API can return a redirect for invalid subreddits. The scripts are designed to handle such redirects without following them.
