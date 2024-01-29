#!/usr/bin/python3
"""Gathers the data feom an API."""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_data = "https://jsonplaceholder.typicode.com/users"
    url = base_data + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_data = url + "/todos"
    response = requests.get(todo_data)
    tasks = response.json()
    total_tasks = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_tasks, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
