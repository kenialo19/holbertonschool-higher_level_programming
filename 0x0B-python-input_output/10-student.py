#!/usr/bin/python3
"""Student to JSON"""


class Student:
        """Class"""
        def __init__(self, first_name, last_name, age):
                """Constructor"""
                self.first_name = first_name
                self.last_name = last_name
                self.age = age

        def to_json(self, wi=None):
            """Method Returns: [type]: dict"""
            if wi is None:
                return self.__dict__
            dict = {}
            for i in wi:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return dict
