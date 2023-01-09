#!/usr/bin/python3
"""
================================
Define the class inherits_from
================================
"""


def inherits_from(obj, a_class):
    """
        checks if object is an instance of a class with
        direct or indirect inheritance and return true.
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
