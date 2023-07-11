#!/usr/bin/python3
import json
"""module contains load_from_json function"""


def load_from_json_file(filename):
    """function creates an object from file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
