#!/usr/bin/python3
"""an object creating function"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
