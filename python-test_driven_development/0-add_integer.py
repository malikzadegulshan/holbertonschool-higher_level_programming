#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles floats by casting them to integers before addition.
It raises a TypeError for any non-integer, non-float inputs.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to int) and returns an integer.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
