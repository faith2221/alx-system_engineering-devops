#!/usr/bin/python3
"""
Prints the titles of the first 10 host posts.
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API,
    prints first 10 hot posts titles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
