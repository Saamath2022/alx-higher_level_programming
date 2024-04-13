#!/usr/bin/python3
"""Module for add_integer method"""


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
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
