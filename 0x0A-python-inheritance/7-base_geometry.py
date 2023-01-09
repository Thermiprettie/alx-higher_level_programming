#!/usr/bin/python3
"""module with class BaseGeometry."""


class BaseGeometry:
    """The class."""

    def area(self):
        """calculate area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate if a number is integer or not."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
