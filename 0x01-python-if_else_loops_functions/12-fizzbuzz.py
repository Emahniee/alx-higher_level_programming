#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            msg = 'FizzBuzz'
        elif num % 3 == 0:
            msg = 'Fizz'
        elif num % 5 == 0:
            msg = 'Buzz'
        else:
            msg = str(num)
        print(f"{num}", end=' ')
