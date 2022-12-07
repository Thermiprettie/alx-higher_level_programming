#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    retkey = list(a_dictionary.keys())[0]
    sta8 = a_dictionary[retkey]
    for k, v in a_dictionary.items():
        if v > sta8:
            sta8 = v
            retkey = k
    return (retkey)
