#!/usr/bin/python3
"""Module 2-is_same_class.
"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class.
    Args:
        - obj: object to look at
        - a_class: class to verify the instance of
    Returns: True if obj is an instance of a_class,
    False otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
