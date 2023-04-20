"""
File: Word Games.py
Author: Zach Southwick

Purpose: To play a madlib game with the user and display their inputs
"""

print('Please enter the following: \n')
adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
print('Please choose an exclamation: ')
print('A - Oh no')
print('B - Shoot')
print('C - Dang')
choice = input().lower()
if choice == 'a':
    choice = 'Oh no'

elif choice == 'b':
    choice = 'Shoot'

elif choice == 'c':
    choice = 'Dang'

verb2 = input('verb: ')
verb3 = input('verb: ')

print('\nYour story is: \n')

print('''The other day, I was really in trouble. It all started when I saw a very
{} {} {} down the hallway. \"{}!\" I yelled. But all
I could think to do was to {} over and over. Miraculously,
that caused it to stop, but not before it tried to {}
right in front of my family.'''.format(adjective.upper(), animal, verb1, choice.title(), verb2, verb3))
print()