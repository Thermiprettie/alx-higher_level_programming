#!/usr/bin/python3
"""Module with class BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialises the attributes."""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
