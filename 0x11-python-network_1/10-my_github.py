#!/usr/bin/python3
"""This script  script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        url, headers={'Authorization': "Bearer {}".format(password)})
    if response.status_code >= 400:
        print(None)
    else:
        jsonData = response.json()
        print(jsonData["id"])
