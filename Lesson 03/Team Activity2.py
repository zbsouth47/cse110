import math

square_length = input('What is the length of the square? ')
square_area = float(square_length) ** 2
print('The area of the square is ' + str(square_area) + '\n')

rect_length = input('What is the length of the rectangle? ')
rect_width = input('What is the width of the rectangle? ')
rect_area = float(rect_length) * float(rect_width)
print('The length of the rectangle is ' + str(rect_area) + '\n')

radius = input('What is the radius of the circle? ')
circ_area = math.pi * (float(radius) ** 2)
print('The area of the cirle is ' + str(circ_area) + '\n')