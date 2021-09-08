#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    sys.path.append('./')
    for i in dir(hidden_4):
        if i[0:2] != "__":
            print(i)
