#!/usr/bin/python3
"""
<<<<<<< HEAD
    python script that exports data in the JSON format
"""
import json
import requests

=======
    exporting data in the JSON format
"""


import json
import requests


>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    """
<<<<<<< HEAD
        export to JSON
=======
        exporting to JSON
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
    """

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
<<<<<<< HEAD
            for u in users}, jsonfile)
=======
            for u in users}, jsonfile)
>>>>>>> ffae77ac608018668f281303944f7e87b3677a11
