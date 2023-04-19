import math

def square(l):
    return float(l) **2

def rectangle(l, w):
    return float(l) * float(w)

def circle(r):
    return math.pi * (float(r) ** 2)
"""
square_length = input('What is the length of the square? ')
print('The area of the square is ' + str(square(square_length)) + '\n')

rect_length = input('What is the length of the rectangle? ')
rect_width = input('What is the width of the rectangle? ')
print('The length of the rectangle is ' + str(rectangle(rect_length, rect_width)) + '\n')

radius = input('What is the radius of the circle? ')
print('The area of the cirle is ' + str(circle(radius)) + '\n')
"""

length = input('What is the length you wish to calculate in centimeters? ')
square_cent = square(length)
square_meter = square(length) / 10000
rect_cent = rectangle(length, length)
rect_meter = rectangle(length, length) / 10000
circ_cent = circle(length)
circ_meter = circle(length) / 10000
print('\nThe area of this square is ' + str(square_cent) + ' centimeters squared and ' + str(square_meter) + ' meters squared.')
print('The area of this rectangle is ' + str(rect_cent) + ' centimeters squared and ' + str(rect_meter) + ' meters squared.')
print('The area of this cirle is ' + str(circ_cent) + 'centimeters squared and ' + str(circ_meter) + ' meters squared.\n')