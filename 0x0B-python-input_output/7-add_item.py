#!/usr/bin/python3
"""Load, add, save"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    txt = load_from_json_file("add_item.json")
except FileNotFoundError:
    txt = list()
for argument in sys.argv[1:]:
    txt.append(argument)
save_to_json_file(txt, "add_item.json")
