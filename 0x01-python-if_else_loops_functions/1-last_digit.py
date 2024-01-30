#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print(f'Last digit of {str(number)} is {str(number[4])} and is not greater than 6')
