#!/usr/bin/python3
"""Module 4-appenD_write.
"""


def append_write(filename="", text=""):
    """Appends text to filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    with open(filename, "a") as f:
        return f.write(text)
