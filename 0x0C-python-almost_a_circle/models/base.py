#!/usr/bin/python3
"""This is class base"""


import json
import turtle


class Base:
    """Class that manage id attribute in all future classes
    and to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method initialize a Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file"""
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(9)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(9, 5)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """File to instances"""
        filename = cls.__name__ + ".json"
        list_obj = []
        try:
            with open(filename, "r") as f:
                list_obj = [cls.create(**d)
                            for d in cls.from_json_string(f.read())]
            return list_obj
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw'''
        turtle.setworldcoordinates(-1, -1, 700, 700)
        t = turtle.Turtle()
        turtle.bgcolor("grey")
        t.color('#33FF4E')
        for i in list_rectangles:
            t.down()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.up()
            t.forward(i.width * 2)

        for j in list_squares:
            t.down()
            t.forward(j.width)
            t.left(90)
            t.forward(j.height)
            t.left(90)
            t.forward(j.width)
            t.left(90)
            t.forward(j.height)
            t.left(90)
            t.up()
            t.forward(j.width * 2)
