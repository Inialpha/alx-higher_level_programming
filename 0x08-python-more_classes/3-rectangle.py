#!/usr/bin/python3
"""module is contains a class that define a Rectangle"""


class Rectangle:
    """class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes object attribute"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """functions get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retives height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        result = ""
        result = ("#" * self.__width + "\n") * self.__height
        if self.__height == 0 or self.__width == 0:
            result = ""
        return result
