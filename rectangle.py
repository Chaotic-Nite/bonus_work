'''
Creating a function that generates a list of tuples with values ranging from 2 to 9. 
The returning result should be a list of tuples sorted from largest enclosed area to smallest.

Formula for enclosed area (w-1)*(h-1) - setup for a function to do calculations
'''

__author__ = "ChaoticNite"


def enclosed_area(w, h):
    return (w-1)*(h-1)


def generate_list():
    return [(j, i) for j in range(2, 10) for i in range(j, 10)]


def rectangle_sort():
    rectangles = generate_list()
    rectangles.sort(key=lambda x: enclosed_area(x[0], x[1]), reverse=True)
    return rectangles


print(rectangle_sort())
