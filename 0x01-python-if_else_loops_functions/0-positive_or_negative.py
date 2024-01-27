#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f" {int(number[4])} +  is positive")
elif number == 0:
    print(str(number) + ' is zero')

else:
    print(str(number) + ' is negative')

