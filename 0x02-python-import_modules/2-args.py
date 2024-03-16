#!/usr/bin/python3

import sys

if __name__ == "__main__":

    count = len(sys.argv)
    if count == 0:
        print("0 argument(s).")
    elif count == 1:
        print("1 argument:)
    else:
        print("{}"argument:".format(count))

        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
