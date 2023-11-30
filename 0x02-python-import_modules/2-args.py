#!/usr/bin/python3
def print_argv():
    argv_len = len(argv)
    if argv_len == 1:
        print('0 arguments.')
    elif argv_len == 2:
        print(f'{argv_len - 1} argument:')
    else:
        print(f'{argv_len - 1} arguments:')

    for i, args in enumerate(argv[1:], start=1):
        print(f'{i}: {args}')


if __name__ == '__main__':
    from sys import argv
    print_argv()
