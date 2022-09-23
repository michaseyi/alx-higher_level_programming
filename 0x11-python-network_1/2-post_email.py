#!/usr/bin/python3
"""This script takes in a URL and an email, sends a PORT request to the
passed URL with the email as a paramerter, displays the body of the
response encoded as utf-8"""
import urllib.request as request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
