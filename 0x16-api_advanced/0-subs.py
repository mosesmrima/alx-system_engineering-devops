#!/usr/bin/python3
"""This script gets number of subscribers from a subreddit"""
import requests
from sys import argv

headers = {"User-Agent": "aUserAgent"}
url = "https://www.reddit.com/subreddits/search.json?q={}"\
    .format(argv[1])
subreddit = requests.get(url, headers=headers).json()

print(subreddit['data']['children'][0]['data']['subscribers'])
