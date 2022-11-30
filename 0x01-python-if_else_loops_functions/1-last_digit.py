#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    difference = number % -10
else:
    difference = number % 10
print('Last digit of', number, 'is', difference, end=' ')
if difference > 5:
    print('and is greater than 5')
elif difference == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
