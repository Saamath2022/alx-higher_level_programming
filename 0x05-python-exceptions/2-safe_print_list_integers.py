#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        t = 0
    for item in my_list[:x]:
        try:
            f isinstance(item, int):
                print("{d:}".format(item), end='')
                t = += 1
        except ValueError:
            pass
        print()
        return t
    except TypeError:
        raise Exception("my_list must be iterable")
    except Exception as e:
        raise Exception("An error ocurred: {}".format(e))
