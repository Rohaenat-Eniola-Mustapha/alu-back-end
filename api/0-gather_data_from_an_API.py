#!/usr/bin/python3

"""Importing module"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    """ Define the base URL for the API """
    base_url = "https://jsonplaceholder.typicode.com"

    """Fetch user data"""
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data["name"]

    """Calculate the number of completed tasks"""
    completed_tasks = [task for task in todos_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    """Print employee information"""
    print(f"Employee {employee_name} is done with tasks
          ({number_of_done_tasks}/{total_number_of_tasks}):")

"""Print completed task titles"""
for task in completed_tasks:
      print(f"\t{task['title']}")