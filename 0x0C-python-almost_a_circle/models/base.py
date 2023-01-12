#!/usr/bin/python3
"""Writing a class Base."""


class Base:
    """The class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiating the attributes."""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
