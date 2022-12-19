#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        intList = 0
        while intList < x:
            print("{:d}".format(my_list[intList]), end="")
            intList += 1
    except (ValueError, TypeError):
        intList += 1
    print()
    return intList
