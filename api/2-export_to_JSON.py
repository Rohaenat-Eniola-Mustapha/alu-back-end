#!/usr/bin/python3
"""
Exporting data in the JSON format.
"""

import json
import requests
from sys import argv

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

    # Exporting to JSON
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)