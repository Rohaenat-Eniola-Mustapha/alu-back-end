#!/usr/bin/python3
"""
Importing modules and gathering data from an API.
"""


import urllib.request
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to fetch TODO data for the specified employee ID
    todo_url = f"{base_url}/todos?userId={employee_id}"
    todo_response = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_response.read().decode())

    # Check if the employee was found
    if not todo_data:
        print("Employee not found")
        sys.exit(1)

    # Calculate the number of completed tasks
    completed_tasks = [
        task for task in todo_data if task["completed"]
        ]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    # Print employee information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = urllib.request.urlopen(user_url)
    user_data = json.loads(user_response.read().decode())
    employee_name = user_data["name"]

    # Print employee information and completed task titles
    print(
        f"Employee {
            employee_name
            } is done with tasks(
                {number_of_done_tasks}/{total_number_of_tasks}
                ):"
        )
    for task in completed_tasks:
        print(f"\t{task['title']}")