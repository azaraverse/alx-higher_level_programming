#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        # try the division
        result = a / b
    except ZeroDivisionError:
        # handle division by zero by passing it, no error message
        pass
        # handle other execptions bound to occur
    except Exception as err:
        print("An error occured: ", err)
    finally:
        # print the result, or None if an execption occured
        print("Inside result: {}".format(result))

    # return the value of the division itself
    # or None if an exception occurred
    return (result)
