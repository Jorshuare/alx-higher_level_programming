#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        return my_list[x - 1]
    except IndexError:
        pass
