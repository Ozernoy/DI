'''
Exercise 1: Formula
Instructions
Write a program that calculates and prints a value according to this given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
For example, if the user inputs: 100,150,180
The output should be:

18,22,24
'''

from math import sqrt

def Q(D, C=50, H=30):
    return int(sqrt((2 * C * D)/H))

l = [int(el) for el in input().split(sep=",")]

for el in l:
    print(Q(el))