#!/usr/bin/python3
""" Models for base class """


class Base:
    """ A hierachy representation for base in
    object oriented programming
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ The constructor intializes the ide attr."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
