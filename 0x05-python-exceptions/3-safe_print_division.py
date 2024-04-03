#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except Exception as e:
        print("An error occured:", e)
        result = None
    finally:
        print("inside result: {}".format(result))
        return result
