#!/usr/bin/python3
"""modue for class BaseGeometry"""


class BaseGeometry:
    """ A clsss 5hat defines geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initializes the objects"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
