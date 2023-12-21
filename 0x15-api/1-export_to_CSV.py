#!/usr/bin/python3
"""
Export data from the given REST API to a CSV file.
"""

import csv
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

    filename = f"{employee_id}.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        for task in tasks:
            csvwriter.writerow(
                [employee_id, username, task['completed'], task['title']])

    print(f"Data exported to {filename}")
