"""
File: Loan Qualification.py
Author: Zach Southwick

Purpose: To see if a user qualifies for a loan
"""

print('Please enter a rating from 1-10 for each of the following: ')
size = int(input('Loan Amount: '))
cred_history = int(input('Credit History: '))
income = int(input('Income: '))
down_payment = int(input('Down Payment: '))
loan_decision = ''

if size >= 5:
    if cred_history >= 7 and income >= 7:
        loan_decision = 'yes'
    elif (cred_history >= 7 or income >= 7) and down_payment >= 5:
        loan_decision = 'yes'
    else:
        loan_decision = 'no'
elif size < 5: 
    if cred_history < 4:
        loan_decision = 'no'
    elif income >= 7 or down_payment >= 7:
        loan_decision = 'yes'
    elif income >= 4 and down_payment >= 4:
        loan_decision = 'yes'
    else:
        loan_decision = 'no'
else:
    loan_decision = 'no'

print(f'Loan decision is {loan_decision}')