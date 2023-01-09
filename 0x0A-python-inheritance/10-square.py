#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Module with class BaseGeometry."""


class Square(Rectangle):
    """a class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialises the attributes."""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """set the area of Rectangle."""

        return self.__size ** 2
