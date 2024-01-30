#!/usr/bin/python3
"""Gathers the data from an API."""


if __name__ == "__main__":
    import json
    import requests
    import sys

    if __name__ == "__main__":
        id = sys.argv[1]

        url_1 = f"https://jsonplaceholder.typicode.com/users/{id}"
        url_2 = "https://jsonplaceholder.typicode.com/todos"

        p = requests.get(url_1)
        content = json.loads(p.content)
        name = content["name"]

        r = requests.get(url_2)
        content_2 = json.loads(r.content)

        titles = []
        done = 0
        total = 0

        for item in content_2:
            if item["userId"] == int(id):
                total += 1
                if item["completed"] is True:
                    titles.append(item["title"])
                    done += 1

        print(f"Employee {name} is done with tasks({done}/{total}):")
        for title in titles:
            print(f"\t {title}")
