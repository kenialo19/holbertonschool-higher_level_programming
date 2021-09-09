#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4, sys
    sys.path.append('./')
    for i in dir(hidden_4):
        if i[0] != "_":
            print("{}".format(i))