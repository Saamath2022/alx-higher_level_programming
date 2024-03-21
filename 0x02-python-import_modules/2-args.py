#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments:")
        print(".")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, arg))
