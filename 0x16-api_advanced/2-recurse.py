#!/usr/bin/python3
"""
Lists 10 hot psts under given subreddit Using recursion
"""

import requests


def recurse(subreddit, hot_list=[]):
    """If no results found, returns None."""
    user = {"User-Agent": "0x16.api_advanced"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            recurse(subreddit, after_data, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
            return hot_list
    else:
        return (None)
