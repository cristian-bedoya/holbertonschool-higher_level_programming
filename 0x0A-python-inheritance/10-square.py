#!/usr/bin/python3
"""Module 8-rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a rectangle.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes an instance.
        Args:
            - size: size of the square
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Computes the area of the Rectangle instance."""
        return self.__size ** 2
