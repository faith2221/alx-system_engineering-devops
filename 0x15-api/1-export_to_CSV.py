#!/usr/bin/python3
"""Gathers the data fron an API and exports it to CSV."""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_data = "https://jsonplaceholder.typicode.com/users"
    url = base_data + "/" + employee_id

    user_response = requests.get(url)
    username = response.json().get('username')

    todo_data = url + "/todos"
    user_response = requests.get(todo_data)
    tasks = response.json()

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get("title')))
