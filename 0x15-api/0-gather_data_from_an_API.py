#!/usr/bin/python3
"""
This script gathers data from an API using urllib
It then serializes the json data to a python dictionary and prints it out
It takes an parameter, the user Id of the user's data that you want
"""
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    completed = 0
    tasks = 0
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        json_data = response.read()
        dict_obj = json.loads(json_data)
        for jsonob in dict_obj:
            if jsonob['completed']:
                completed += 1
                tasks += 1
            else:
                tasks += 1
    url = 'https://jsonplaceholder.typicode.com/users?id={}'\
        .format(sys.argv[1])
    with urllib.request.urlopen(url) as user_details:
        user_data = user_details.read()
        user_dict = json.loads(user_data)
        for data in user_dict:
            name = data['name']
    output = "Employee {} is done with tasks({}/{}):".format(name, completed,
                                                             tasks)
    print(output)
    for task in dict_obj:
        if task['completed']:
            print("\t{}".format(task['title']))
