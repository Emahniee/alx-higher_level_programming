#!/usr/bin/python3
'''Module for task 2'''



def is_same_class(obj, a_class):
    '''Checking if object is exactly an instance of the specified class'''
    if type(obj) == a_class:
        return True
    else:
        return False
