#!/usr/python3
def safe_print_list_integers(my_list=[], x=0):
    try
    t_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            t_print += 1
        except ValueError:
            pass
    print("")
    return (t_print)
