#!/usr/bin/python3
"""rectangle class"""


class Rectangle:

    """Public class attribute"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor Method for Rectangle """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            new_string += str(self.print_symbol) * self.__width
            if x < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """Returns a String with a representation
        of the state of the object"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """printthe message at deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
