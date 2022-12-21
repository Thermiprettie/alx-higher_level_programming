#!/usr/bin/python

"""create class named Square"""


class Square:
    """Class created."""

    def __init__(self, size):
        """Initializing the square.

        Args:
            size (int): Size of the created Square.
        """
        self.size = size

    @property
    def size(self):
        """retrieve the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
