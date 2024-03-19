#!/usr/bin/python3
def delet_at(my_list=[], indx=0):
    if idx >= len(my_list):
        print("{} out of range".format(indx))
    else:
        del my_list[idx]
        print("deleted item at position", idx)
