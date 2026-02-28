#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A class that inherits from list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
