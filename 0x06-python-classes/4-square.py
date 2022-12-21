#!/usr/bin/python3

"""Create a class: Square."""


class Square:
    """The new Square created."""

    def __init__(self, size=0):
        """Initializing the new square.

        Args:
            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """to retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area."""
        return (self.__size * self.__size) # A public instance method
