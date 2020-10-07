#!/usr/bin/python3
"""Module 2-read_lines
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file:
        - filename: name of the file
    """

    with open(filename) as f:
        n_lines = 0
        i = 0
        for lines in f:
            n_lines += 1

        f.seek(0)
        if nb_lines <= 0 or nb_lines >= n_lines:
            read_text = f.read()
            print(read_text, end="")
        else:
            for line in f:
                print(line, end='')
                i += 1
                if i == nb_lines:
                    break
