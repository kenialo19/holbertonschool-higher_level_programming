#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        while counter < x:
            print("{}".format(my_list[counter]), end="")
            counter += 1
    except IndexError:
        print("")
    finally:
        return counter
