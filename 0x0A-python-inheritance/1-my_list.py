#!/usr/bin/python3
"""
========================
Module with class MyList
========================
"""


class MyList(list):
    """a class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """prints the list, sorted in ascending order"""

        print(sorted(list(self)))
