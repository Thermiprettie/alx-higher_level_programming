#!/usr/bin/python3
"""Define the function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
