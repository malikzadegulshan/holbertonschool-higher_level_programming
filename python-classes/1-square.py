#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square with the given size.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
