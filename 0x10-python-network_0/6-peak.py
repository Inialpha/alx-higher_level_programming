#!/usr/bin/python3
"""module implement a peak finding algorithm"""


def find_peak(list_of_integers):
    """A peak findung algorithm"""

    lenght = len(list_of_integers)
    if lenght == 0:
        return None

    for n in range(lenght):
        try:
            if list_of_integers[n] >= list_of_integers[n - 1]\
                    and list_of_integers[n] >= list_of_integers[n + 1]:
                return list_of_integers[n]
        except IndexError:
            pass
