#!/usr/bin/python3
"""Class Rectangle """


class Rectangle:
    """Represents a Rectangle.
    Private instance attribute: width:
        - property def width(self)
        - property def height(self)
        - property setter def width(self, value)
        - property setter def height(self, value)
    Instantiation with optional width and height.

    """

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Print informal the rectangle with the character #"""
        if self.__height is 0 or self.__width is 0:
            return ''
        n_string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                n_string += '#'
            n_string += '\n'
        return n_string[:-1]

    def __repr__(self):
        """ Return a string representation of the rectangle
        to be able to recreate
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))
