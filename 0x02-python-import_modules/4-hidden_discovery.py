#!/usr/bin/python3

if _ _ name_ _ == "_ _main_ _":

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] !_ "__":
            print(name)
