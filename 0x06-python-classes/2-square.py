#!/usr/bin/python3

''' Square form '''


class Square:
    ''' Class with constructor'''

    def __init__(self, size=0):
        '''constructor square'''
        self.__size = size
        try:
           type(size) != int or size < 0
        except (TypeError, ValueError):
            print("size must be an integer")
            print("size must be >= 0")
