#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
    print("--")
