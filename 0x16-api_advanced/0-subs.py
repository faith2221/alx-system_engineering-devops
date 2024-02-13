#!/usr/bin/python3
"""
Function that queries the Reddit API and returns number of subscribers.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
