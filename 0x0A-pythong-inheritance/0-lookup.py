#!/usr/bin/python3
"""DEfine the Function """
# Define the function
def lookup(obj):
    return dir(obj)

# Example usage
class MyClass:
    def __init__(self):
        self.attribute1 = 10

    def method1(self):
        pass

obj = MyClass()
print(lookup(obj))
