#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for a in range(1, len(argv)):
        print("{}: {}".format(a, argv[a]))
