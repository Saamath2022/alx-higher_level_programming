#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """print a name

    Args:
        frist_name (str): The first name to be printed.
        last_name (stri): the last name to print

    Raises:
        TypeError: if either of first_name or last_name are not strings    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/3-say_my_name.txt")
