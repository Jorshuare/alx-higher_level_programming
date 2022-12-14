#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, weight = 0, 0
    for i in my_list:
        v_1, v_2 = i
        avg += v_1 * v_2
        weight += v_2
    return avg / weight
