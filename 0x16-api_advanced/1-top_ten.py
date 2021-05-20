#!/usr/bin/python3
"""This script gets number of subscribers from a subreddit"""
import requests
import sys


def top_ten(subreddit):
    headers = {
        "User-Agent": "aUserAgent"
    }
    params = {
        'limit': 10
    }
    url = "https://www.reddit.com/r/{}/hot.json"\
        .format(subreddit)
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)
    status_code = response.status_code
    if status_code != 200:
        print(None)
    else:
        response_json = response.json().get('data')
        [print(c.get("data").get("title"))
         for c in response_json.get("children")]
