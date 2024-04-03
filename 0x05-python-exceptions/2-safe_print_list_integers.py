#!/usr/bin/python3

ef safe_print_list_integers(my_list=[], x=0):
    try:
        nb_print = 0
        for item in my_list[:x]:
            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end='')
                    np_print += 1
            except ValueError:
                pass
        print()
        return nb_print
    except typeError:
        raise Exception("my_list must be iterable")
    except Exception as e:
        raise Exception("An error occureed: {}".format(e))
