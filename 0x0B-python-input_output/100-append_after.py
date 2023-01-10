#!/usr/bin/python3
"""Write function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """insert line of text to a file."""
    some_text = ""
    with open(filename) as r:
        for line in r:
            some_text += line
            if search_string in line:
                some_text += new_string
    with open(filename, "wrt") as wrt:
        wrt.write(text)
