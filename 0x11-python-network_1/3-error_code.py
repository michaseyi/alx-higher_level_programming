#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and displays the
body of the response if no error else the error code"""
import urllib.request as request
import urllib.parse
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
