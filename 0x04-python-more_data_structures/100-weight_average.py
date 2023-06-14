#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    average = 0
    weights = 0
    for item in my_list:
        average += (item[0] * item[1])
        weights += item[1]
    return average / weights

# my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
# result = weight_average(my_list)
# print("Average: {:0.2f}".format(result))
