#!/urs/bin/pthon3
"""A rectangle class Module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class"""

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
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """Method for validating the value."""
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{value} must be >= 0")
        elif not eq and value <= 0:
            raise ValueError(f"{value} must be > 0")

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle by printing it to stdout using the '#' character.
        """
        for _ in range(self.y)
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

     def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args (int): The values to update the attributes in the order:
            id, width, height, x, y.
            **kwargs (int): The key/value pairs to update the attributes.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
