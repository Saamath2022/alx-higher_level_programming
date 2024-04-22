#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Class representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__y = value

    def validate_integer(self, name, value, eq=True):
    """Method for validating the value"""
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if eq and value < 0:
        raise ValueError("{} must be >= 0".format(name))
    elif not eq and value <= 0:
        raise ValueError("{} must be > 0".format(name))

