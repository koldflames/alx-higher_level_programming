#!/usr/bin/python3
""" Class that defines a Rectangle """


class Rectangle:
    """
    Defines a rectangle by the following args (private instance attributes):
    width (int)
    height (int)
    Instantiation with optional width and height
    """

    def __init__(self, width=0, height=0):
        """ Initializing the rectangle class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets width attribute """
        return self.__width

    @property
    def height(self):
        """ gets height attribute """
        return self.__height

    @width.setter
    def width(self, value):
        """ set width property """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height property """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
