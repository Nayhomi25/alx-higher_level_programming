#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
