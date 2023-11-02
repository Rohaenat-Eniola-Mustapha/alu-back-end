#!/usr/bin/python3
"""
Python script that exports data in CSV format.

Usage: python3 export_to_CSV.py <employee_id>
"""

import csv
import json
import requests
from sys import argv


def main():
    """
    Retrieve user information and export their TODO list to a CSV file.
    """
    employee_id = argv[1]

    # Request user information by employee ID
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = json.loads(user_response.text)
    username = user_data.get("username")

    # Request user's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = json.loads(todo_response.text)
    
    # Create a dictionary to store task status (completed) in boolean format
    tasks = {}

    # Loop through the TODO list and get completed tasks
    for todo in todo_data:
        tasks.update({todo.get("title"): todo.get("completed")})

    # Export to CSV
    with open(f'{employee_id}.csv', mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for title, completed in tasks.items():
            csv_writer.writerow([employee_id, username, completed, title])

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        exit(1)

    main()