#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avrg = 0
    dvde = 0
    for t in my_list:
        avrg += t[0] * t[1]
        dvde += t[1]
    return float(avrg / dvde)
