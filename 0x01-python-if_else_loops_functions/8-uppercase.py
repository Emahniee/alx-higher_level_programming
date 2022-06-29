#!/usr/bin/python3
def uppercase(str):
    for a in str:
        letter = ord(a)
        if  letter >= 65 and letter <= 90:
            print(a, end='')
        elif letter >= 97 and letter <= 122:
            print("{}".format(chr(letter - 32)), end='')
