#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ''
        n_new = ''
        for i in range(len(my_string)):
            if my_string[i] == 'C' or my_string[i] == 'c':
                new_string = my_string[:i] + my_string[i + 1:]
                for j in range(len(new_string)):
                    if new_string[j] == 'C' or new_string[j] == 'c':
                        n_new = new_string[:j] + new_string[j + 1:]
                        return n_new
                    else:
                        continue
        return new_string
