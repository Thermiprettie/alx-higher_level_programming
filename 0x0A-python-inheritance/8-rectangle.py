#!/usr/bin/python3
"""To write a class rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """A class named rectangle."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
