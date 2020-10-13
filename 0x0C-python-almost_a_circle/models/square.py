#!/usr/bin/python3
"""Module Square.
Create a Square class, inheriting from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """create  class Square that inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overriding the __str__ method """
        string = '[Square] ({:d}) {:d}/{:d} - {:d}'\
            .format(self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the y attribute."""
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Updates attributes of an instance."""
        l_args = ["id", "size", 'x', 'y']

        if args is not None and len(args) != 0:
            for arg_idx in range(len(args)):
                setattr(self, l_args[arg_idx], args[arg_idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        dict1 = {'id': self.id, 'size': self.width, 'x':
                 self.x, 'y': self.y}
        return dict1
