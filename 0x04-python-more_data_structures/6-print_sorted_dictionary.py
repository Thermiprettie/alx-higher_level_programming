#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for t in sorted(a_dictionary):
        print("{:s}: {}".format(t, a_dictionary[t]))
