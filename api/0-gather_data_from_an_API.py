#!/usr/bin/python3

# import from urllib, json and sys
import urllib.request
import json
import sys

# check whether the script is run as the main program 
if __name__ == "__main__":
    # check if the there is exactly one command-line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = urllib.request.urlopen(user_url)
    user_data = json.loads(user_response.read().decode())

    # Fetch TODO list data
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = urllib.request.urlopen(todos_url)
    todos_data = json.loads(todos_response.read().decode())

    if "id" not in user_data:
        print("Employee not found")
        sys.exit(1)

    employee_name = user_data["name"]

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Print employee information
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

    # Print completed task titles
    for task in completed_tasks:
        print(f"\t{task['title']}")
