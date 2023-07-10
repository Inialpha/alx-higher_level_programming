#!/usr/bin/python3
"""mo$ue for MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __new__(cls, *args, **kwargs):
        """creates new class instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

        """initializes objects"""
        self.__value = value

    def __eq__(self, other):
        """handle equality"""
        return int(self) != other

    def __ne__(self, other):
        """change  == to !="""
        return int(self) == other
