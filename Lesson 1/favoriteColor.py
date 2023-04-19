"""
Program: favoriteColor.py
Author: Zach Southwick

Purpose: To ask the user questions and display the answers back to them.
"""
name = input('What is your name: ')
favoriteColor = input ('What is your favorite color: ')
age = input('How many years old are you: ')
location = input('Where are you from: ')
print('Hi ' + name + '!')
print('Your favorite color is ' + favoriteColor + '.')
if favoriteColor == 'green':
    print('Green is my favorite color too!')
print('You are currently ' + age + ' years old.')
print('You are from ' + location + '.')
print('Thanks for chatting with me!')