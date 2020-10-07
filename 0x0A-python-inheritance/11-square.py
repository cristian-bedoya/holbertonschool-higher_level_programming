#!/usr/bin/python3
"""Module 8-rectangle."""


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
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns a formatted string."""
        super().__str__()

    def area(self):
        """Computes the area of the Rectangle instance."""
        return self.__size ** 2
