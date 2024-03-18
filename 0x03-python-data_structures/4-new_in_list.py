#!/usr/bin/python3
def get_element_or_copy(my_list=[], idx=0):
    if idx < 0:
        return my_list.copy()
    elif idx < len(my_list):
        return my_list[idx]
    else:
        return Nonei
