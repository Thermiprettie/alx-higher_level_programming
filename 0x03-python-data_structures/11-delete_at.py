#!/usr/bin/python3
def delete_at(my_list=[], sta8=0):
    if sta8 < 0 or sta8 >= len(my_list):
        return my_list
    my_list.remove(my_list[sta8])
    return my_list
