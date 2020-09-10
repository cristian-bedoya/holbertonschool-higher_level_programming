#!/usr/bin/python3
def common_elements(set_1, set_2):
    ele_cmmn = list(set_1 - (set_1 - set_2))
    return ele_cmmn
