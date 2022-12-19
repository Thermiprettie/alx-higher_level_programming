#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        intdiv = a / b
        return intdiv
    except ZeroDivisionError:
        intdiv = None
    finally:
        print("Inside result: {}".format(div))
