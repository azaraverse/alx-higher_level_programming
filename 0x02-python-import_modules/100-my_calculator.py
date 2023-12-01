#!/usr/bin/python3
def print_calc():
    argv_len = len(sys.argv)
    operator = ['+', '-', '*', '/']
    if argv_len != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif sys.argv[2] == '/':
        print('{:d} / {:d} = {:.0f}'.format(a, b, div(a, b)))
    else:
        if sys.argv[2] not in operator:
            print('Unknown operator. Available operators: +, -, *, and /')
            exit(1)


if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    print_calc()
