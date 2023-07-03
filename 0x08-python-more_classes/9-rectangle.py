#!/usr/bin/python3
"""module is contains a class that define a Rectangle"""


class Rectangle:
    """class defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes object attribute"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """calculate the parameter"""
        if self.__height == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """print the string representation"""
        result = ""
        return "\n".join([str(self.print_symbol)
                         * self.__width] * self.__height)
        if self.__height == 0 or self.__width == 0:
            result = ""
        return result

    def __repr__(self):
        """print the official represantation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """compares the area of rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        r_1 = rect_1.area()
        r_2 = rect_2.area()
        if r_2 > r_1:
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        """creats a new instance of class"""
        return Rectangle(size, size)
