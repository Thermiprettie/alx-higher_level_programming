#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    aList = []
    for i in range(list_length):
        try:
            listdiv = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            listdiv = 0
        except IndexError:
            print("out of range")
            listdiv = 0
        except ZeroDivisionError:
            print("division by 0")
            listdiv = 0
        finally:
            aList.append(listdiv)
    return aList
