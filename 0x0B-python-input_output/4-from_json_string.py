#!/usr/bin/python3
"""module contains from_json_sring funcion"""
import json


def from_json_string(my_str):
    """deserializes a json string"""
    return json.loads(my_str)
