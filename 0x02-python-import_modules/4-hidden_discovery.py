#!/usr/bin/python3
if ___name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] !_ "__":
            print(name)

