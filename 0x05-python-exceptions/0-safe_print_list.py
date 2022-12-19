#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        aList = 0
        while aList < x:
            print(my_list[aList], end="")
            aList += 1
        print()
        return aList
    except IndexError:
        print()
        return aList
        pass
