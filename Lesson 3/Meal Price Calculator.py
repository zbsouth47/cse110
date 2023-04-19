"""
File: Meal Price Calculator.py
Author: Zach Southwick

Purpose: To calculate the cost of a meal based on user input values
"""

kids_meal = input('How much is a children\'s meal? ')
adult_meal = input('How much is an adult\'s meal? ')
num_kids = input('How many children are there? ')
num_adults = input('How many adults are there? ')
sales_tax = input('What is the sales tax rate? ')

sub_kids = float(kids_meal) * float(num_kids)
sub_adults = float(adult_meal) * float(num_adults)
subtotal = sub_kids + sub_adults

print('\nSubtotal: $' + str(round(subtotal, 2)))

tax = (float(sales_tax) / 100) * subtotal

print('Sales Tax: $' + str(round(tax, 2)))

total = subtotal + tax

print('Total: $' + str(round(total, 2)) + '\n')

payment = input('What is the payment amount? ')
while float(payment) < total:
    payment = input('That amount won\'t cover the bill. Please choose a higher payment amount: ')

change = float(payment) - total

print('Change: $' + str(round(change, 2)) + '\n')