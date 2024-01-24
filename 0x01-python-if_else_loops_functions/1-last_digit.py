#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[4] > 0 and number[4] < 6:
    print(f'Last digit of {number} is {number[4]} and is not greater than 6')
