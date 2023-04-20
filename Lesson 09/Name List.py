"""
file: Name List.py
author: Zach Southwick

purpose: Gather a list of the user's friends and display it back to them
"""

friends =[]
friend_name = ''

while friend_name != 'end':
    friend_name = input('Type the name of a friend: ')
    friends.append(friend_name)

print('\nYour friends are:')
for friend in friends:
    if friend != 'end':
        print(friend.capitalize())

print()