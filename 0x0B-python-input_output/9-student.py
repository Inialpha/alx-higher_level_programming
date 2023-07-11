#!/usr/bin/python3
"""module contians Student class"""


class Student:
    """describes students"""
    def __init__(self, first_name, last_name, age):
        """initializes class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a dictionary representation.of object"""

        return self.__dict__
