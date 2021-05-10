#!/usr/bin/python3
"""
This script gathers data from an API using urllib
It then serializes the json data to a python dictionary and prints it out
It takes an parameter, the user Id of the user's data that you want
"""
if __name__ == "__main__":
    import urllib.request
    import json
    import sys

    completed = 0
    total_tasks = 0

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com/todos?userId={}'.format(sys.argv[1])) as response:
        json_data = response.read()
        dict_obj = json.loads(json_data)
        for jsonob in dict_obj:
            if jsonob['completed']:
                completed += 1
                total_tasks += 1
            else:
                total_tasks += 1

    with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users?id={}'.format(sys.argv[1])) as user_details:
        user_data = user_details.read()
        user_dict = json.loads(user_data)
        for data in user_dict:
            name = data['name']

    print("Employee {} is done with tasks({}/{}):".format(name, completed, total_tasks))
    for task in dict_obj:
        if task['completed']:
            print("\t{}".format(task['title']))
