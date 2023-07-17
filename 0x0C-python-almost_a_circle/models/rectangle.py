#!/usr/bin/python3
"""module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the value of widt"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """for retriving width"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retreive th value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints a representation of the rectangle"""
        [print() for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x,)]
            print("#" * self.__width)

    def __str__(self):
        """return details about a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                 self.id, self.__x, self.__y,
                                                 self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates a rectangle"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is not None:
                        self.id = arg
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg

                i += 1
        else:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "id":
                        if value:
                            self.id = value
                        else:
                            self.__init__(self.width, self.
                                          height, self.x, self.y)
                    elif key == "width":
                        self.__width = value
                    elif key == "height":
                        self.__height = value
                    elif key == "x":
                        self.__x = value
                    elif key == "y":
                        self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
