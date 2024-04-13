#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # Split text by delimiter
        parts = text.split(delim)
        # Join parts with delimiter and two new lines
        text = (delim + "\n\n").join(parts)
    print(text, end="")


if __name__ == "__main__":
    """Importing the doctest module"""
    import doctest
    """ Running the test cases from the specified file"""
    doctest.testfile("tests/5-text_indentation.txt")
