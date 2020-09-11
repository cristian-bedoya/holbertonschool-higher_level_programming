#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_n = 0
    li = list(map(lambda x: rom_d.get(x), roman_string))
    for i in range(len(li)):
        if i > 0 and li[i] > li[i - 1]:
            rom_n = li[i] - 2 * li[i - 1]
        else:
            rom_n += li[i]
    return rom_n
