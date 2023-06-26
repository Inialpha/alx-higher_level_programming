#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ln = 0
    for i in range(x):
        ln += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print()
            return ln
    print()
    return ln
