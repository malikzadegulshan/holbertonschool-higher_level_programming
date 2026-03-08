#!/usr/bin/python3
"""Module that defines a Student class with serialization and deserialization."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary."""
        for k, v in json.items():
            setattr(self, k, v)
