"""
File: While Examples.py
Author: Zach Southwick

Purpose: Practice while loops
"""

num = -1

num = int(input('Please type a positive number: '))
while num < 0:
    print('Sorry, that is a negative number. Please try again.')
    num = int(input('Please type a positive number: '))
    
print(f'The number is: {num}')

candy = 'no'

candy = input('May I please have a piece of candy? ')
while candy.lower() != 'yes':
    candy = input('May I please have a piece of candy? ')

print('Thank you.')