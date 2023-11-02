#!/usr/bin/python3
"""
This script retrieves and displays a user's
TODO list progress using a REST API.

Usage: python3 gather_data_from_api.py <employee_id>
"""

import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (str): The ID of the employee.

    Returns:
        None
    """
    # Construct URLs for user and TODO data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={
        employee_id
        }"

    try:
        # Fetch user and TODO data from the API
        user_info = requests.get(user_url).json()
        todo_info = requests.get(todo_url).json()

        # Extract employee name and completed tasks
        employee_name = user_info.get("name")
        completed_tasks = [task for task in todo_info if task["completed"]]
        compl_count = len(completed_tasks)
        ttl_count = len(todo_info)

        # Display the progress information
        print(
            f"Employee {employee_name} is done with tasks({compl_count}/{ttl_count}):"
            )
        for task in completed_tasks:
            print(f"\t{task['title']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_api.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress(employee_id)