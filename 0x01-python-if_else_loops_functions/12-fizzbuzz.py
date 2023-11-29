#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if 0 == i % 15:
            print('FizzBuzz', end=' ')
        elif 0 == i % 5:
            print('Buzz', end=' ')
        elif 0 == i % 3:
            print('Fizz', end=' ')
        else:
            print('{}'.format(i), end=' ')
