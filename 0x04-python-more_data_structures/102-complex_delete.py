#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_to_delete = []
    for keys, values in a_dictionary.items():
        if values == value:
            key_to_delete.append(keys)
    for key in key_to_delete:
        del a_dictionary[key]
    return a_dictionary
