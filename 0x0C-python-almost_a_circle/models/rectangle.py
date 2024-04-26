#!/usr/bin/python3
"""Module for models base functions"""
import json

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

if __name__ == "__main__":
    with open("rectangle_data.json") as f:
        data = json.load(f)
        obj = Rectangle(**data)
        print("Width:", obj.width)
        print("Height:", obj.height)
        print("X:", obj.x)
        print("Y:", obj.y)
        print("ID:", obj.id)
