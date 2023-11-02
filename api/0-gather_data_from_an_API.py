#!/usr/bin/python3
"""
Gather data from an API using the requests module.

This script fetches TODO list data for a specific employee ID and displays
the progress of completed tasks.

Usage: python 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

def get_todo_list_progress(employee_id):
    """
    Fetches and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com/'

    try:
        user_response = requests.get(f'{base_url}users/{employee_id}')
        user_data = user_response.json()
        employee_name = user_data['name']

        todos_response = requests.get(f'{base_url}todos?userId={employee_id}')
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        total_tasks = len(todos_data)
        completed_task_count = len(completed_tasks)

        print(f'Employee {employee_name} is done with tasks({completed_task_count}/{total_tasks}):')
        for task in completed_tasks:
            print(f'\t{task["title"]}')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_api.py <employee_id>')
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_list_progress(employee_id)