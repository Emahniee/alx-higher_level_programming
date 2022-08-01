#!/usr/bin/python3

'''Module for task 3'''



def is_kind_of_class(obj, a_class):
    '''True if the object is an instance of current class, or a class current class inherited from'''
    return isinstance(obj, a_class)
