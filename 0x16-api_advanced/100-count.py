#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Recursively queries the Reddit API, parses titles of hot articles, and
    counts occurrences of given keywords. Returns a sorted count of keywords.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'my_user_agent'}
    params = {'after': after} if after else {}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']
    if not posts:
        word_count = {}
        for word in word_list:
            word_count[word] = 0
        for title in hot_list:
            for word in word_list:
                if word.lower() in title.lower().split():
                    word_count[word] += 1
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print(f"{word.lower()}: {count}")
        return

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    count_words(subreddit, word_list, hot_list, after)
