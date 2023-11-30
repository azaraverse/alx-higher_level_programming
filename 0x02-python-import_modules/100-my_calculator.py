#!/usr/bin/python3

def calc():
    argv_len = len(sys.argv)
    operator = ['+', '-', '*', '/']
    if argv_len != 4:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[2] not in operator:
        print('Unknown operator. Available operators: +, -, *, /')
        sys.exit(1)


def print_calc():
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    else:
        print('{:d} / {:d} = {:.0f}'.format(a, b, div(a, b)))


if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    calc()
    print_calc()
