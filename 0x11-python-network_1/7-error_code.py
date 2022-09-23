#!/usr/bin/python3
"""This scripttakes in a URL, sends a request
to the URL and displays the body of the response."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
