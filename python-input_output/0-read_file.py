#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file to stdout."""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")