'''
Creating a function that generates a list of tuples with values ranging from 2 to 9. 
The returning result should be a list of tuples sorted from largest enclosed area to smallest.

Formula for enclosed area (w-1)*(h-1) - setup for a function to do calculations
'''

__author__ = "ChaoticNite"

import random


def enclosed_area(w, h):
    return (w-1)*(h-1)


def generate_list(amount):
    tuples_list = []
    while len(tuples_list) < amount:
        tuples_list.append((random.random(2, 10), random.randint(2, 10)))
    return tuples_list


def rectangle_sort():
    # rectangles = generate_list(10)
    pass
    