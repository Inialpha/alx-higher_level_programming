#!/usr/bin/python3
"""module contains load_from_json function"""
import json


def load_from_json_file(filename):
    """function creates an object from file"""
    with open(filename, "r", encoding="UTF-8") as f:

        return json.load(f)
