#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the square.
        """
        self.size = size

        @property
        def size(self):
            """Get/set the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of tne square"""
        return (self.__size * self.__size)
