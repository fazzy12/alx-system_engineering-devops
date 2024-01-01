#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given
    subreddit. If the subreddit is invalid or not found, returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_user_agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the response is successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
