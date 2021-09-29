"""A class Square that defines a square"""


class Square:
    """init allow square class to be used"""
    def __init__(self, size=0):
        """asign private instance attribute size"""
        self.__size = size

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
