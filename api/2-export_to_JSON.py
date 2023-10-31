#!/usr/bin/python3
"""
    exporting data in the JSON format
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """
        requesting user info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        converting json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        extracting username
    """
    username = user.get("username")

    """
        requesting user's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status in boolean format
    """
    tasks = {}
    """
        converting json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        looping through dictionary & get completed tasks
    """
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
    """
        exporting to JSON
    """
    with open('{}.json'.format(argv[1]), mode='w') as file:
        json.dump(json_to_dump, file)