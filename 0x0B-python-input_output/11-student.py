#!/usr/bin/python3
"""Write a class Student."""


class Student:
    """Class Student."""

    def __init__(self, first_name, last_name, age):
        """Instantiating the attributes for Students."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """obtain dictionary representation."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance."""
        for k, v in json.items():
            setattr(self, k, v)
