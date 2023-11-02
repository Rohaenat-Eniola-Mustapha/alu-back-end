#!/usr/bin/python3
"""
Importing modules and gathering data from an API.
"""


import requests
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


def main():
    """
    Main function for the script.

    The script accepts an employee ID as a command-line argument and
    retrieves information about the employee's TODO list progress.
    It then prints the information in the specified format.
    """
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    data = fetch_todo_data(employee_id)
    user_data = data["user_data"]
    todos_data = data["todos_data"]

    employee_name = user_data["name"]

    completed_tasks = [task for task in todos_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    print(
        f"Employee {
            employee_name
            } is done with tasks(
                {
                    number_of_done_tasks
                    }/{
                        total_number_of_tasks
                        }
                ):"
        )

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    main()