#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    result = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except TypeError:
            ans = 0
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            ans = 0
            print("{}".format("division by 0"))
        except IndexError:
            ans = 0
            print("{}".format("out of range"))
        finally:
            result.append(ans)
    
    return result

