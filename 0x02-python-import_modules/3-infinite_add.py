#!/usr/bin/python3
def add_argv():
    sum = 0
    for i, args in enumerate(argv[1:]):
        sum += int(args)
    print('{}'.format(sum))


if __name__ == '__main__':
    from sys import argv
    add_argv()
