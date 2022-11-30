#!/usr/bin/python3
def fizzbuzz():
    for t in range(1, 101):
        if t % 3 is 0 and t % 5 is 0:
            print("FizzBuzz ", end='')
        elif t % 3 is 0:
            print("Fizz ", end='')
        elif t % 5 is 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(t), end='')
