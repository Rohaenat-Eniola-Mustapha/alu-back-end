#!/usr/bin/python3
"""
<<<<<<< HEAD
    python script that exports data in the JSON format
"""
=======
Exporting data in the JSON format.
"""


>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
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
=======

if __name__ == "__main__":
    # Requesting user info by employee ID
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))

    # Converting JSON to a dictionary
    user = json.loads(request_employee.text)

    # Extracting the username
    username = user.get("username")

    # Requesting user's TODO list
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    # Dictionary to store task status in boolean format
    tasks = {}

    # Converting JSON to a list of dictionaries
    user_todos = json.loads(request_todos.text)

    # Looping through dictionaries and getting completed tasks
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    task_list = []
    for k, v in tasks.items():
        task_list.append({
            "task": k,
            "completed": v,
            "username": username
        })

    json_to_dump = {argv[1]: task_list}
<<<<<<< HEAD
    """
        export to JSON
    """
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)
=======

    # Exporting to JSON
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
