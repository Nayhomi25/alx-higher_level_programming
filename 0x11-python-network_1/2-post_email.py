#!/usr/bin/python3
"""script that takes in a URL and an email sends a POST request to the URL"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = urlencode(value).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        print(response.read().decode())
