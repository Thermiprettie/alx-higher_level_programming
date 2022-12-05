#!/usr/bin/python3

def element_at(my_list, sta8):
    if sta8 < 0:
        return None
    if sta8 >= len(my_list):
        return None
    return my_list[sta8]
