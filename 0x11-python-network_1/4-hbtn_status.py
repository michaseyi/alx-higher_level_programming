#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status and prints out
a formated output"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    data = response.text
    print("Body response:")
    print("    - type: {}".format(type(data)))
    print("    - content: {}".format(data))
