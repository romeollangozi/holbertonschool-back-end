#!/usr/bin/python3
"""
Model to make a request to an
API and retrieve data
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    res = requests.get(f"{URL}users/{argv[1]}")
    res = res.json()
    user_name = res['username']

    res = requests.get(f"{URL}todos")
    all_todos = res.json()
    user_todos = [todo for todo in all_todos if todo['userId'] == int(argv[1])]

    with open(f"{user_id}.csv", 'w') as csv:
        for todo in all_todos:
            first = f'"{user_id}","{user_name}",'
            csv.write(f'{first}"{todo["completed"]}","{todo["title"]}"\n')
