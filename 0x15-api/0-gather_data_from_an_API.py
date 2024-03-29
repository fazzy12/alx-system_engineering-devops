#!/usr/bin/python3
"""This module provides functionality to retrieve and
display TODO list progress for a given employee ID using a REST API."""

import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])

    base_url = "https://jsonplaceholder.typicode.com"

    response = requests.get(f"{base_url}/users/{employee_id}")

    employee_data = response.json()
    name = employee_data.get("name")

    response = requests.get(f"{base_url}/todos?userId={employee_id}")

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    finish = len(completed_tasks)

    print(f"Employee {name} is done with tasks({finish}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task['title']}")
