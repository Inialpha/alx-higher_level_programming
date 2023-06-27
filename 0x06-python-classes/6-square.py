#!/usr/bin/python3

""" a class Square that defines a square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes class"""

        self.position = position
        self.size = size

    @property
    def position(self):
        """retives the value of size"""
        return self.__size

    @position.setter
    def position(self, value):
        """set the value of size"""
        if type(value) is tuple and len(value) == 2 and\
                value[0] >= 0 and value[1] >= 0:

            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """retives the value of size"""
        return self.__size

    @size.setter
    def size(self, value):

        """set the value of size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value

            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """defines the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints the squarex"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
