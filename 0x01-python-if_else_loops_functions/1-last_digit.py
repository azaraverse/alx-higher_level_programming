#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10


def main():
    print(f'Last digit of {number} is', end=' ')

    if number >= 0:
        last_digit = number % 10
    else:
        if number % 10 != 0:
            last_digit = -10 + (number % 10)
        else:
            last_digit = 0

    print(f'{last_digit} and is', end=' ')
    if last_digit > 5:
        print('greater than 5')
    elif last_digit == 0:
        print('0')
    elif last_digit < 6 and last_digit != 0:
        print('less than 6 and not 0')


main()
