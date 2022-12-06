#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    else:
        if idx > len(my_list):
            return my_list
        else:
            new = [i for i in my_list]
            new[idx] = element
            return new
