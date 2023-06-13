#!/usr/bin/python3
"""A file writing function"""


def write_file(filename="", text=""):
    """Writes a string into a textfile"""
    with open(filename, "w", encoding="utf-8") as f:
        return(f.write(text))
