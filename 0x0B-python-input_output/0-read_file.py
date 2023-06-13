#!/usr/bin/python3
"""Module: 0-read_file.py"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, encoding="utf-8") as a:
        print(a.read(), end="")
