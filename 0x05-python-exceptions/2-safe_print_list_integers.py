#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t_print, b = 0, 0
    while t_print < x:
        try:
            if isinstance(my_list[t_print], int):
                print("{:d}".format(my_list[t_print]), end='')
                b += 1
        except (ValueError, TypeError):
            pass
        t_print += 1
    print()
    return b
