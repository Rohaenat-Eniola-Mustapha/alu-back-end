#!/usr/bin/python3
"""
A Python script that exports data in CSV format.
"""


import requests
import csv
import sys


def fetch_todo_data(employee_id):
    """
    Fetch TODO list data for a specific employee.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        dict: A dictionary containing TODO list information.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return {
        "user_data": user_data,
        "todos_data": todos_data
    }


def export_to_csv(employee_id, user_data, todos_data):
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": user_data["name"],
                "TASK_COMPLETED_STATUS": "True" if task[
                    "completed"
                    ] else "False",
                "TASK_TITLE": task["title"]
            })

if __name__ == "__main__":
    """
    This script accepts an employee ID as a command-line argument and
    retrieves information about the employee's TODO list progress.
    It then exports the data to a CSV file in the specified format.

    Usage: python 0-gather_data_from_an_API.py <employee_id>
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    data = fetch_todo_data(employee_id)
    user_data = data["user_data"]
    todos_data = data["todos_data"]

    export_to_csv(employee_id, user_data, todos_data)

    print(f"Data exported to {employee_id}.csv")