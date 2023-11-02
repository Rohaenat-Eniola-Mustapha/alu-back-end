#!/usr/bin/python3
<<<<<<< HEAD
""" Import libraries """
=======
"""
This script retrieves and displays a user's TODO list 
progress using a REST API.
Usage: python3 gather_data_from_api.py <employee_id>
"""
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11

import requests
import sys

<<<<<<< HEAD
"""Gathering data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_name = user_info.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
    task_com = len(total_tasks)
    total_task_done = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    [print("\t {}".format(task.get("title"))) for task in total_tasks]
=======

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
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Fetch user and TODO data from the API
        user_info = requests.get(user_url).json()
        todo_info = requests.get(todo_url).json()

        # Extract employee name and completed tasks
        empl_name = user_info.get("name")
        completed_tasks = [task for task in todo_info if task["completed"]]
        compl_count = len(completed_tasks)
        ttl_count = len(todo_info)

        # Display the progress information
        print(f"Employee {empl_name} is done with tasks({compl_count}/{ttl_count}):")

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
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
