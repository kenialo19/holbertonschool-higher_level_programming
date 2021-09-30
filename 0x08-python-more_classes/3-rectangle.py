#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """
    Class rectangle that defines a
    rectangel by based on 0-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """ Constructor Method for Rectangle """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instnace attributte: width  """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instnace attributte: height  """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the Rectangle Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        new_string = ""
        for x in range(self.__height):
            new_string += "#" * self.__width
            if x < self.__height - 1:
                new_string += "\n"
        return new_string
