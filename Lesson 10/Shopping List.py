"""
file: Shopping List.py
author: Zach Southwick

purpose: Gather the user's shopping list
"""

item = ''
shopping_list = []

print('Please enter the items of the shopping list (type: quit to finish): ')
item = input('Item: ')
while item.lower() != 'quit':
    shopping_list.append(item)
    item = input('Item: ')

print('The shopping list is: ')
for i in range(len(shopping_list)):
    count = i + 1
    print(f'{count}. {shopping_list[i].capitalize()}')

switch = int(input('Which item would you like to change? ')) - 1
shopping_list[switch] = input('What is the new item? ')

print('The new shopping list is: ')
for i in range(len(shopping_list)):
    count = i + 1
    print(f'{count}. {shopping_list[i].capitalize()}')