#!/usr/bin/python3
"""Dwefines a function for text insertion"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    text = ""

    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)
