def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            counter += 1
        except(TypeError, ValueError):
            pass
    print()
    return counter
