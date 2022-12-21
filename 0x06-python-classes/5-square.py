#!/usr/bin/python3
"""Define a Square class"""

class Square:
    """Define a Square
    Attributes:
    _size (int): the size side of a square
    """
    def __init__(self, size=0):
        ''' Initializes an instance of the Square class
        Args:
            size (int): the size of 1 side of a square
        Returns:
            None
        '''
        self.__size = size

    def area(self):
        """Calculate the area of a Sqaure instance
        Returns:
            the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size attribute of a class instance
        Returns:
            the size of a square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets the size attribute of a square instance
        Args:
            value: the value to set size to
        '''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__Size = value

    def my_print(self):
        count = self.__size
        if count == 0:
            print()
        for i in range(count):
            for i in range(count):
                print("#", end="")
            print()

