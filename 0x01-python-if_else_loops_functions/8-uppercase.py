#!/usr/bin/python3

def uppercase(str):
    res_str = ''
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            res_str += chr(ord(c) - ord('a') + ord('A'))
        else:
            res_str += c
    print('{}'.format(res_str))
