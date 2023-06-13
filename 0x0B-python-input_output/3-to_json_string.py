#!/usr/bin/python3
"""A json conversion functions"""
import json


def to_json_string(my_obj):
    """This function returns the json representation of a string"""
    return json.dumps(my_obj)
