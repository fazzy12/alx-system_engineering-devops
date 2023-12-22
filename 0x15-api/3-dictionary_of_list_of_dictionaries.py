#!/usr/bin/python3
"""
Exports data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    all_data = {}
    for user in users:
        user_id = str(user.get('id'))
        all_data[user_id] = []

        for task in todos:
            if task.get('userId') == int(user_id):
                task_data = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                }
                all_data[user_id].append(task_data)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file)
