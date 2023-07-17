#!/usr/bin/python3
"""module for the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for height and width"""
        self.width = value
        self.height = value

    def __str__(self):
        """prints details of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the instance attributes"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
