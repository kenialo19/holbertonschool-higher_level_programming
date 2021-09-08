#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    sys.path.append('./')
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i][0:2] != "__":
            print (names[i])       
