#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            j += 1
        except:
            pass
    print()
    return j
