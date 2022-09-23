#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status and prints out
a formated output"""
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(data.decode('utf-8')))
