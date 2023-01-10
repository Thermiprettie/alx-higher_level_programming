#!/usr/bin/python3
"""Write a class that defines a student."""


class Student:
    """The class."""

    def __init__(self, first_name, last_name, age):
        """Instantiating the student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method to retrieve a dictionary rep of a Student instance."""
        return self.__dict__
