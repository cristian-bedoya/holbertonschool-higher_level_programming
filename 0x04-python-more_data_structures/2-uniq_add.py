#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    sum_ele = 0
    for x in new_list:
        sum_ele += x
    return sum_ele
