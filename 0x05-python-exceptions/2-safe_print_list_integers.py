#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t_print = 0
    try:
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                t_print += 1
        except TypeError:
            pass
        except IndexError:
            raise IndexError("Index out of range")
        print()
        return t_print
    except Exception as e:
        raise Exception("An error occured:{}".format(e))
