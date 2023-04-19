import math

def rectangle(l, w):
    return l * w

def square(l):
    #return l ** 2
    return rectangle(l, l)

def circle(r):
    return math.pi * (r ** 2)

def compute_area(shape, length, width = 0):
    if shape.lower() == 'circle':
        area = circle(length)
    elif shape.lower() == 'square':
        area = square(length)
    elif shape.lower() == 'rectangle':
        area = rectangle(length, width)
    else: 
        area = 'invalid'
    return area

shape = input('What shape do you have (circle, square, rectangle)? ')
while shape.lower() != 'quit':
    if shape.lower() == 'circle':
        length = float(input('Please enter the radius of the circle: '))
        area = compute_area(shape, length)
        #area = circle(length)                                                                      #These two lines met the core requirements
        #print(f'The area of a circle with radius {length} is {area:.2f}')                          #Removed in favor of the new code
    elif shape.lower() == 'square':
        length = float(input('Pleae enter the length of one side of the square: '))
        area = compute_area(shape, length)
        #area = square(length)                                                                      #These two lines met the core requirements
        #print(f'The area of a square with length {length} is {area:.2f}')                          #Removed in favor of the new code
    elif shape.lower() == 'rectangle':
        length = float(input('Pleae enter the length the rectangle: '))
        width = float(input('Pleae enter the width of the rectangle: '))
        area = compute_area(shape, length, width)
        #area = rectangle(length, width)                                                            #These two lines met the core requirements
        #print(f'The area of a rectangle with length {length} and width {width} is {area:.2f}')     #Removed in favor of the new code
    else: 
        print('That is not a valid shape. Please try again.')

    print(f'The area for your input values is {area:.2f}')
    shape = input('What shape do you have (circle, square, rectangle, quit to exit)? ')