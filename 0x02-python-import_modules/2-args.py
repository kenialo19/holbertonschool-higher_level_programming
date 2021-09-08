#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print("{} arguments.".format(a - 1))
    else:
        print("{} arguments:".format(a - 1))
    for x in range(1, a):
        print("{}: {}".format(x, argv[x]))
