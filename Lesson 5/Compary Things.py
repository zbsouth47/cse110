"""
File: Compary Things.py
Author: Zach Southwick

Purpose: To demonstrate understanding of 'if' statements
"""


num1 = float(input('Please enter a number: '))
num2 = float(input('Please enter another number: '))

print()
if num1 > num2:
    print('The first number is greater')
else:
    print('The first number is not greater')

if num1 == num2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if num1 < num2:
    print('The second number is greater')
else:
    print('The second number is not greater')


fav_animal = input('\nWhat is your favorite animal? ')
my_fav = 'peregrin falcon'

if fav_animal.lower() == my_fav:
    print('That\'s my favorite animal too!')
else:
    print('That one is not my favorite.')