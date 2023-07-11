#!/usr/bin/python3
"""module contains class_to_json(obj) function"""


def class_to_json(obj):
    """return a dictionary description"""
    return obj.__dict__
