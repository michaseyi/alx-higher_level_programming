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
    params = {"per_page": 10}
    response = requests.get(url, params=params)
    try:
        commits = response.json()
        commits.sort(key=lambda x: x["commit"]["author"]["date"], reverse=True)
        for commit in commits:
            sha = commit["sha"]
            author = commit["commit"]["author"]["name"]
            date = commit["commit"]["author"]["date"]
            print("{}: {}".format(sha, author))
    except ValueError:
        ...
