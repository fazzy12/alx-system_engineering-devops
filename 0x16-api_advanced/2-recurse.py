#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to collect titles of all hot articles
    for a given subreddit. Returns a list of titles or None if the subreddit
    is invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'my_user_agent'}
    params = {'after': after} if after else {}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not posts:
            if not hot_list:
                return None
            else:
                return hot_list
        else:
            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
    else:
        return None
