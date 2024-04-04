#!/usr/bin/python3

def safe_function(fct, *args):
    import syst
    try:
        tc = fct(*args)
        return tc
    except Exception as e:
        print("exception: {}".format(e).stderr)
        return NOne
