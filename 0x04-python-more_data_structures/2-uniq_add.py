#!/usr/bin/python3
def uniq_add(my_list=[]):
    to_add = set(my_list)
    otpt = 0
    for i in to_add:
        otpt += i
    return otpt
