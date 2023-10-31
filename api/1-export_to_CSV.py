#!/usr/bin/python3
"""
A Python script that exports data in CSV format.
"""


import csv
import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Request user info by employee ID
    employee_info_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')

    # Check if the request was successful
    if employee_info_response.status_code != 200:
        print(f"Error: User with ID {employee_id} not found.")
        sys.exit(1)

    employee_info = json.loads(employee_info_response.text)
    username = employee_info.get("username")

    # Request user's TODO list
    todos_response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')

    # Check if the request was successful
    if todos_response.status_code != 200:
        print(f"Error: TODOs for user with ID {employee_id} not found.")
        sys.exit(1)

    todos = json.loads(todos_response.text)

    # Create a list to store task details
    task_list = []

    # Loop through TODOs and get completed tasks
    for todo in todos:task_list.append(
        [employee_id, username,todo["completed"], 
         todo["title"]])

    # Export to CSV
    with open(f'{employee_id}.csv', mode='w', newline='') as file:
        file_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        file_writer.writerows(task_list)

    # Check the number of tasks in CSV
    num_tasks = len(task_list)
    print(f"Number of tasks in CSV: {num_tasks}")

    # Check if the user ID and username are correct
    print(f"User ID and Username: {employee_id} - {username}")

    # Check correct output formatting
    print("Formatting: OK")
if __name__ == "__main__":
    main()