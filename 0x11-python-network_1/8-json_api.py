#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    response = requests.post(url, {"q": q})
    try:
        jsonData = response.json()
        if jsonData == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsonData["id"], jsonData["name"]))
    except ValueError:
        print("Not a valid JSON")
