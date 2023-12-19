#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This module provides functionality to retrieve and
display TODO list progress for a given employee ID using a REST API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

"""


import requests
import sys


def fetch_employee_data(id):
    """
    Fetch the TODO list progress for a given employee ID from the API.

    Parameters:
    - employee_id (int): The ID of the employee for whom to fetch the data.

    Returns:
    - dict: A dictionary containing the employee's name, number of completed
    tasks, total tasks, and the list of completed task titles.

    Raises:
    - ValueError: If the employee ID is not an integer or if there's an
    issue fetching data from the API.

    """

    url = "https://jsonplaceholder.typicode.com"
    response = requests.get(f"{url}/users/{id}")
    if response.status_code != 200:
        print("Error fetching employee data")
        return None

    employee_data = response.json()
    employee_name = employee_data.get("name")

    response = requests.get(f"{url}/todos?userId={id}")
    if response.status_code != 200:
        print("Error fetching TODO list")
        return None

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo["completed"]]
    num_completed_tasks = len(completed_tasks)

    return {
        "name": employee_name,
        "num_completed_tasks": num_completed_tasks,
        "total_tasks": total_tasks,
        "completed_tasks": [todo["title"] for todo in completed_tasks]
    }


def display_employee_progress(employee_data):
    """
    Display the TODO list progress of the employee in the specified format.

    Parameters:
    - employee_data (dict): A dictionary containing the employee's name,
    number of completed tasks, total tasks, and the list
    of completed task titles.

    Returns:
    - None

    """
    if not employee_data:
        return

    name = employee_data["name"]
    num_completed_tasks = employee_data["num_completed_tasks"]
    total_tasks = employee_data["total_tasks"]
    completed_tasks = employee_data["completed_tasks"]

    print(
        f"Employee {name} is done with tasks({
            num_completed_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    id = int(sys.argv[1])
    employee_data = fetch_employee_data(id)
    display_employee_progress(employee_data)
