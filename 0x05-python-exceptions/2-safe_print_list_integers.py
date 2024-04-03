#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        nb_print = 0
        for item in my_list[:x]:
            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end='')
                    np_print += 1
            except (ValueError, TypeError):
                pass
        print()
        return nb_print
    except Exception as e:
        print("An error occurred:", e)
        return None
