#!/usr/bin/python3
'''Class rectangle'''


class Rectangle:
    '''Form'''

    def __init__(self, width=0, height=0):
        '''Constructor'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        '''Get the height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
    def __str__(self):
        '''Rectangle like a string'''
        if self.__height == 0 or self.__width == 0:
            return ''
        return '{}{}'.format(('#' * self.__width + '\n') * (h - 1), '#' * self.__width)
