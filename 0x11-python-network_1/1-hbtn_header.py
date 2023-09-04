#!/usr/bin/python3
""" sends a request to the URL and displays the value of the X-Request-Id"""
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
