#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Class describing a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Method Constuctor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y attribute."""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle instance.
        """
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character # """
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ Overriding the __str__ method """
        string = '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """Updates attributes of an instance."""
        l_args = ['id', 'width', 'height', 'x', 'y']

        if args is not None and len(args) != 0:
            for arg_idx in range(len(args)):
                setattr(self, l_args[arg_idx], args[arg_idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        dict1 = {'id': self.id, 'width': self.__width, 'height':
                 self.__height, 'x': self.__x, 'y': self.__y}
        return dict1
