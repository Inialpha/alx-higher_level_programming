#!/usr/bin/python3
"""modle contians save_to json function"""
import json


def save_to_json_file(my_obj, filename):
    """function writes a json rep to  file"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
