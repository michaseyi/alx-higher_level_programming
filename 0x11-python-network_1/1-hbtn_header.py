#!/usr/bin/python3
"""This script fetches in the URL passed as the first command line
argument and prints the value of the X-Request-Id header"""
import urllib.request as request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
