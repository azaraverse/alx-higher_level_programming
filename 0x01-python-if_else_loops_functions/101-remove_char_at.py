#!/usr/bin/python3

def remove_char_at(str, n):
    cpy = ''
    if len(str) == 0:
        return str
    for i in range(len(str)):
        if i != n:
            cpy += str[i]
    return cpy
