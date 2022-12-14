#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    for key, values in a_dictionary.items():
        if values == value:
            del_keys.append(key)
    for i in del_keys:
        del a_dictionary[i]
    return a_dictionary
