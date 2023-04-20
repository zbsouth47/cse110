"""
File: Numeric Data Types.py
Author: Zach Southwick

Purpose: Practice math and type conversions
"""

age = input('How old are you this year? ')
year_older = int(age) + 1
print('Next year you will be ' + str(year_older) + ' years old.\n')

cartons = input('How many egg cartons do you have? ')
eggs = int(cartons) * 12
print('You have ' + str(eggs) + ' eggs.\n')

cookies = input('How many cookies do you have? ')
people = input('How many people are there? ')
fraction = float(cookies) / float(people)
print('Each person will get ' + str(fraction) + ' cookies.\n')