#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    sys.path.append('/mnt/c/Users/winda/kenialo/holbertonschool-higher_level_programming/0x02-python-import_modules')
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][0:2] != "__":
            print (names[i])       
