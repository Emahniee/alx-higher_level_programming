#!/usr/bin/python3
'''Module for task 0'''


def read_file(filename=""):
    '''Read the contents of a file and print to stdout'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
