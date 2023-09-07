#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator(a, operator, b):
    print('{:d} {:s} {:d} = '.format(a, operator, b), end='')

    if operator == '+':
        print('{:d}'.format(add(a, b)))
    elif operator == '-':
        print('{:d}'.format(sub(a, b)))
    elif operator == '*':
        print('{:d}'.format(mul(a, b)))
    elif operator == '/':
        print('{:d}'.format(div(a, b)))


if __name__ == "__main__":
    n = len(sys.argv) - 1

    if n != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    operators = ['+', '-', '*', '/']

    if sys.argv[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    calculator(a, sys.argv[2], b)
