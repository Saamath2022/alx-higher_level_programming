#!/usr/bin/python3
"""Module for add_integer method"""

import doctest


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: the first integer
        b: the second integer, default is 98.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not ininstance(a, float))):
        raise TypeError("a must be an integer or float")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    """ Run doctests from a specified file"""
    doctest.testfile("./tests/0-add_integer.txt")
