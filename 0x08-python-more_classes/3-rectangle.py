#!/usr/bin/python3
"""
A rectangle with width and height.
"""


class Rectangle:
    """
    Rectangle functions and data
    """

    def __init__(self, width=0, height=0):
        """
        Instantiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Functions
    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res
