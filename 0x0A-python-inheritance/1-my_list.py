#!/usr/bin/python3
"""Module 1-my_list."""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
