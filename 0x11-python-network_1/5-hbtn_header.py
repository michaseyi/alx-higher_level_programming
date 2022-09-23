#!/usr/bin/python3
"""This script uses sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id', None))
