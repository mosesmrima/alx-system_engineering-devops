#!/usr/bin/python3
"""This script gets number of subscribers from a subreddit"""
import requests
import sys


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "aUserAgent"}
    url = "https://www.reddit.com/subreddits/search.json?q={}"\
        .format(subreddit)
    response = requests.get(url, headers=headers).json()
    try:
        return response['data']['children'][0]['data']['subscribers']
    except IndexError:
        return 0
