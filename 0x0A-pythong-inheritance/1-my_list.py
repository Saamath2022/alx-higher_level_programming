#!/usr/bin/python3

class MyList(list):
    """A custom list class that inherits from list."""

    def print_sorted(self):
        """Print the list in sorted order (ascending)."""
        sorted_list = sorted(self)  # Sort the list in ascending order
        print(sorted_list)
