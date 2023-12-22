#!/usr/bin/python3
"""
Export data from the given REST API to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username', 'Unknown')
    tasks = todos_data

    data_to_export = {
        employee_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            } for task in tasks
        ]
    }

    filename = f"{employee_id}.json"

    with open(filename, 'w') as jsonfile:
        json.dump(data_to_export, jsonfile)

    print(f"Data exported to {filename}")
