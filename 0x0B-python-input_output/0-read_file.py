#!/usr/bin/python3
"""define a function that reads a text file."""


def read_file(filename=""):
    """reads a UTF8 text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
