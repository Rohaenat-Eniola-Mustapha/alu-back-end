#!/usr/bin/python3
"""
<<<<<<< HEAD
    python script that exports data in the CSV format
"""
=======
Python script that exports data in CSV format.

Usage: python3 export_to_CSV.py <employee_id>
"""

>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
import csv
import json
import requests
from sys import argv


<<<<<<< HEAD
if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        extract username
    """
    username = user.get("username")

    """
        request user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status(completed) in boolean format
    """
    tasks = {}
    """
        convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        export to CSV
    """
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([argv[1], username, v, k])
=======
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
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
