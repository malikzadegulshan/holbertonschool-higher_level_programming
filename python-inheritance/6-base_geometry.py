#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base geometry class with an unimplemented area method."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
