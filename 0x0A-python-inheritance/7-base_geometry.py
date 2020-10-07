#!/usr/bin/python3
"""Module 6-base_geometry."""


class BaseGeometry:
    """Class with public instance method."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
