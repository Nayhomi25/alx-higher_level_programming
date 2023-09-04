#!/usr/bin/python3
"""script that takes in a URL and an email sends a POST request to the URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
