#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{} : {}".format(key, a_dictionary[key]))


#    for key, value in sorted(a_dictionary.items()):
#        new_dict = key
#       print("{} : {}".format(key, value))
