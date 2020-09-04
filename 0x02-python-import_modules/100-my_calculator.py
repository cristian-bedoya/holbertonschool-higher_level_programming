#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    n_args = len(argv) - 1
    if n_args != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = argv[1]
    b = argv[3]
    op = argv[2]
    if op == '+':
        print('{:s} + {:s} = {:d}'.format(a, b, add(int(a), int(b))))
    elif op == '-':
        print('{:s} - {:s} = {:d}'.format(a, b, sub(int(a), int(b))))
    elif op == '*':
        print('{:s} * {:s} = {:d}'.format(a, b, mul(int(a), int(b))))
    elif op == '/':
        print('{:s} / {:s} = {:d}'.format(a, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
