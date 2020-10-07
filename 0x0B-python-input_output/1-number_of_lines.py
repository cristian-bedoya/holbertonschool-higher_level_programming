#!/usr/bin/python3
"""Module 1-number_of_lines
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file
    Args:
        - filename: name of the file
    """
    with open(filename) as f:
        i = 0
        for line in f:
            i += 1
        return i
