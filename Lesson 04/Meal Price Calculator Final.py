"""
File: Meal Price Calculator final.py
Author: Zach Southwick

Purpose: To calculate the cost of a meal based on user input values
"""

num_apps = 0
cost_apps = 0
tip = 0

kids_meal = input('How much is a children\'s meal? ')
adult_meal = input('How much is an adult\'s meal? ')
num_kids = input('How many children are there? ')
num_adults = input('How many adults are there? ')

apps = input('Did you purchase any appetizers? (y/n) ')
if apps == 'y':
    num_apps = input('How many appetizers did you purchase? ')
    cost_apps = input('How much do appetizers cost? ')

sales_tax = input('What is the sales tax rate? ')

sub_kids = float(kids_meal) * float(num_kids)
sub_adults = float(adult_meal) * float(num_adults)
sub_apps = float(num_apps) * float(cost_apps)
subtotal = sub_kids + sub_adults  + sub_apps

print(f'\nSubtotal: ${subtotal:.2f}')

tip_choice = input('Would you like to include a tip? (y/n) ')
if tip_choice == 'y':
    tip_perc = input('What percentage tip would you like to leave? ')
    tip = subtotal * (float(tip_perc) / 100)
    print(f'Tip: ${tip:.2f}')
tax = (float(sales_tax) / 100) * subtotal

print(f'Sales Tax: ${tax:.2f}')

total = subtotal + tip + tax 


print(f'Total: ${total:.2f}\n')

payment = input('What is the payment amount? ')
while float(payment) < total:
    payment = input('That amount won\'t cover the bill. Please choose a higher payment amount: ')

change = float(payment) - (total)

print(f'Change: ${change:.2f}\n')