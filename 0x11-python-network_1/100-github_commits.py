#!/usr/bin/python3
"""This script fetches 10 commits from the repository name and owner
name provided and sortes them from recent to oldest"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1],
        sys.argv[2]
    )
    params = {"per_page": 10, "page": 1}
    response = requests.get(url, params=params)
    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    except BaseException:
        pass
