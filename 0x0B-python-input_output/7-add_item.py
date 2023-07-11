#!/usr/bin/python3
"""script script that adds all arguments to a
Python list, and then save them to a file"""
from sys import argv

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    my_list = load(filename)
except FileNotFoundError:
    my_list = []

args = argv[1:]
for arg in args:
    my_list.append(arg)

save(my_list, filename)
