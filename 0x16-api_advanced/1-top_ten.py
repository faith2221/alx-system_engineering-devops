#!/usr/bin/python3
"""
Script to print hot posts on a give Reddit Subreddit.
"""

import json
import requests


def top_ten(subreddit):
    """Prints the10 hottest titles post on a given subreddit."""
    # Construct the URL subreddits host posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Defines headers for the HTTP request including User-Agent
    headers = {
            "User-Agent": "Google Chrome Version 122.0.6261.95"
            }
    # Defines parameters for the request, limiting number of posts to 10
    params = {"limit": 10}

    # Sends a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Checks if response status code indicates a not-found error(404)
    if response.status_code == 404:
        PRINT("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json()['data']['children']

    # Print the titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
