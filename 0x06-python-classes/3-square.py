#!/usr/bin/python3

"""Create class, Square"""


class Square:
    """Represent a class named Square."""

    def __init__(self, size=0):
        """Initializes the Square.

        Args:
            size (int): size of the Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """For the square area."""
        return (self.__size * self.__size)
