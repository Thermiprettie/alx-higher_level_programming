#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    intList = 0
    errors = 0
    while intList < x:
        try:
            print("{:d}".format(my_list[intList]), end="")
            intList += 1
        except (ValueError, TypeError):
            intList += 1
            errors += 1
        intList -= errors
        print()
        return intList
