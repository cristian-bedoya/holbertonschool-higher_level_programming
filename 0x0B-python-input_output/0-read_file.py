#!/usr/bin/python3
"""Module 0-read_file.
"""


def read_file(filename=""):
    """Reads from filename and prints
    its contents to stdout.
    Args:
        - filename: name of the file
    """
    with open(filename) as f:
        read_f = f.read()
        print(read_f, end="")
