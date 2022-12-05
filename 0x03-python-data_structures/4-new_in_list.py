#!/usr/bin/python3
def new_in_list(my_list, sta8, element):
    if sta8 < 0:
        return my_list
    if sta8 >= len(my_list):
        return my_list
    t_list = list(my_list)
    t_list[sta8] = element
    return t_list
