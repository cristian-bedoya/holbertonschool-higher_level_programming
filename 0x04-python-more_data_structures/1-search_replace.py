#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        if search < 0 or search > (len(my_list) - 1):
            return my_list
        new_list = my_list.copy()
        new_list[search - 1] = replace
        return new_list
