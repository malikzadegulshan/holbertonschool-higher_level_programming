#!/usr/bin/python3
"""
This module provides a function that prints a square using the # character.
It validates the size argument strictly, distinguishing between TypeError
and ValueError depending on the type and value of the input.
"""


def print_square(size):
    """
    Prints a square of # characters of the given size.
    Raises TypeError if size is not an integer, or if it is a negative float.
    Raises ValueError if size is a negative integer.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
