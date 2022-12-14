#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, weight = 0, 0
    if len(my_list) = 0:
        return 0
    else:
        for i in my_list:
            v_1, v_2 = i
            avg += v_1 * v_2
            weight += v_2
    return avg / weight
