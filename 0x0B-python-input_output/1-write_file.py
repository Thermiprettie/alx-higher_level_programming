#!/usr/bin/python3
"""Define a function that writes file."""


def write_file(filename="", text=""):
    """Write string to UTF8 file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
