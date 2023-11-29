#!/usr/bin/python3

new_c = 0
def main():
    for c in range(ord('z'), ord('`'), - 1):
        if c % 2 == 0:
            new_c = c
        else:
            new_c = c - 32
        print('{}'.format(chr(new_c)), end='')
main()
