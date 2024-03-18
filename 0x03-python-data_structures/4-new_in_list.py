#!/usr/bin/python3
def get_element_or_copy(my_list=[], idx=0):
    if idx < 0:
        return my_list.copy()
    elif idx < len(my_list):
        modified_list = my_list.copy()
        modified_list[idx] = 9
        return modified_list
    else:
        return None
