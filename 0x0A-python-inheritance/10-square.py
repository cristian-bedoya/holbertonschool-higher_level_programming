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
        self.__size = size
        super().__init__(self.size, self.size)
        super().integer_validator("size", size)

    def __str__(self):
        return super().__str__()

    def area(self):
        """Computes the area of the Rectangle instance."""
        return self.__size ** 2
