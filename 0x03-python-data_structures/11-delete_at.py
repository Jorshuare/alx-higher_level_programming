#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for i in my_list:
            if i == my_list[idx]:
                continue
            else:
                new_list.append(i)
    return new_list
