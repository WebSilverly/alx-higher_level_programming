#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 1:
    print(f'Last digit of {str(number)} is {str(number[4])}')
