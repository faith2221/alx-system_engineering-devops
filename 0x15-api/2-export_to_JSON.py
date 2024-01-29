#!/usr/bin/python3
"""Gathers the data fron an API and exports it to CSV."""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_data = "https://jsonplaceholder.typicode.com/users"
    url = base_data + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_data = url + "/todos"
    response = requests.get(todo_data)
    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
            })
    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)
