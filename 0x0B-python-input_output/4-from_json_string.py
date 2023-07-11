#!/usr/bin/python3
import json
"""module contains from_json_sring funcion"""


def from_json_string(my_str):
    """deserializes a json string"""
    return json.loads(my_str)
