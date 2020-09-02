#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
if last_digit > 5:
    end = 'greater than 5'
elif last_digit == 0:
    end = '0'
else:
    end = 'less than 6 and not 0'
print("Last digit {:d} is {:d} and is {}".format(number, last_digit, end))
