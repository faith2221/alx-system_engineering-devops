#!/usr/bin/python3
"""
Script to print hot posts on a give Reddit Subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the10 hottest titles post on a given subreddit."""
    # Construct the URL subreddits host posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    # Defines headers for the HTTP request including User-Agent
    headers = {
            "User-Agent": "Google Chrome Version 122.0.6261.95"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        results = response.json()['data']['children']
        [print(post['data']['title']) for post in results]
    else:
        print(None)
