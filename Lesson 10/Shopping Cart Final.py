"""
file: Shopping Cart Final.py
author: Zach Southwick

purpose: Capture user's shopping cart data and display it back to them
"""

item_list = []
item = ''
price_list = []
price = 0.00

def add_item():
    item = input('\nWhat item would you like to add? ')
    price = float(input(f'What is the price of \'{item.title()}\'? '))
    item_list.append(item)
    price_list.append(price)
    print(f'\'{item.title()}\' has been added to the cart')

def view_cart():
    print()
    for i in range(len(item_list)):
        num = i + 1
        print(f'{num}. {item_list[i].title()} - ${price_list[i]:.2f}')

def remove_item():
    remove = int(input('\nWhich item would you like to remove? '))
    remove -= 1
    if remove > len(item_list):
        print('\nThe list is not that long. Please try again.')
    else:
        item_list.pop(remove)
        price_list.pop(remove)
        print('Item removed.')

def compute_total():
    sum = 0
    count = 0
    for p in price_list:
        sum += p
        count += 1
    print(f'\nThe total price for the {count} items in the shopping cart is ${sum:.2f} ')

action = 0
while action != 5:
    print('\nPlease select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = int(input('Please enter an action: '))

    if action < 1 or action > 5:
        print('That is not a valid option. Please try again. ')
    elif action == 1:
        add_item()
    elif action == 2:
        view_cart()
    elif action == 3:
        remove_item()
    elif action == 4: 
        compute_total()

print('Thank you. Goodbye')