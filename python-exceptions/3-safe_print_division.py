#!/usr/bin/python3
def safe_print_division(a, b):
    # start with no result
    result = None

    try:
        # try to divide a by b
        result = a / b

    except ZeroDivisionError:
        # if b is 0, we can't divide, so result stays None
        result = None

    finally:
        # always print the result, whether it worked or not
        print("Inside result: {}".format(result))

    # return the result
    return result
