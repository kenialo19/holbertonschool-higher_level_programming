#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """inicilited size"""
        self.__size = size

        try:
            self.__position = position
        except TypeError as error:
            print(error)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """ this function prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format(" " * self.__position[0]), end="")
                print("{}".format("#" * self.__size))
