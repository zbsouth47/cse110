"""
File: ID Badge.py
Author: Zach Southwick

Purpose: To format a user's id from their inputs
"""

first = input('First Name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job = input('Job title: ')
id_number = input('ID Number: ')
hair = input('Hair color: ')
eye = input('Eye color: ')
month = input ('Starting month: ')
training = input('Training completed (y/n): ')

print('The ID Card is:')
print('-------------------------------------')
print(last.upper() + ', ' + first.capitalize())
print(job.title())
print('ID: ' + id_number)
print()
print(email.lower())
print(phone)
print()
print('{:20}'.format('Hair: ' + hair) + 'Eyes: ' + eye)
print('{:20}'.format('Month: ' + month.title()) + 'Training: ' + training)
print('-------------------------------------')