#!/usr/bin/python3
"""An append file defining function"""


def append_write(filename="", text=""):
    """Appends a string to a utf-8 textfile"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
