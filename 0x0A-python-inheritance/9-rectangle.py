#!/usr/bin/python3
"""Class Rectangle with inheritance from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class with inheritance."""

    def __init__(self, width, height):
        """Method for initialising attributes."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

        def area(self):
            """Method to redefine a area method in the parent class"""

            return self.__width * self.__height

        def __str__(self):
            """__str__ method for return the next string"""
            string = "[" + str(self.__class__.__name__) + "] "
            string += str(self.__width) + "/" + str(self.__height)
            return string
