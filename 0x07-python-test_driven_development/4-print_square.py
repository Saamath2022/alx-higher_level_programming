#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """print a square with the #character.
    Args:
        size (int): the height/width of the square
    Raises:
    Typerror: If size is not an integer
    ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
