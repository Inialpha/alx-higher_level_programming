#!/usr/bin/python3
"""module for to_json_string function"""
import json


def to_json_string(my_obj):
    """for serializing objects"""
    return json.dumps(my_obj)
