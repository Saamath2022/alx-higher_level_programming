#!/usr/bin/python3
"""A square class Module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, width, hight, x=0, y=0, id=None):
        """
        Initialize a square.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    def to_dictionary(self):
        """Return the dictionary representation of the rectangle.
        """
        return {
                'id': self.id
                'width': self.width,
                'height': self.height
                'height': self.height
                'x': self.x,
                'y': self.y
               }

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute. """
        self.validate_integer("width", value, False)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the attributes of the square 
        args: 
        (int) The values to update the attributes in order
        **kwargs (int) the key/value pairs to update the attributes
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwards.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
