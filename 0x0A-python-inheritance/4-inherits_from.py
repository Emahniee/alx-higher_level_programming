#!/usr/bin/python3
'''Module for task 4'''


def inherits_from(obj, a_class):
    '''True if the object is an instance of a class that inherited (directly or indirectly) from the specified class, else False'''
    return issubclass(obj, a_class)
