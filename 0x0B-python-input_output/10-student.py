#!/usr/bin/python3
"""module contians Student class"""


class Student:
    """describes students"""
    def __init__(self, first_name, last_name, age):
        """initializes class object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation.of object"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
