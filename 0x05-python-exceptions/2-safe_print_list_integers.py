#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t, i = 0, 0
    while t < x:
        try:
            print("(:d)".format(my_list[t]), end='')
            i += 1
        except (ValueError, TypeError):
            pass
        t += 1
        print()
        return i
