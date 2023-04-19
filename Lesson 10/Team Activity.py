account_names = []
balances = []
sum = 0
largest = 0

print('Enter the names and balances of bank accounts (type: quit when done)')
name = input('What is the name of this account? ')                              #asking for the first entry outside the loop prevents me from storing the exit 'key' in my list
while name.lower() != 'quit':
    account_names.append(name)
    balance = float(input('What is the balance? '))                             #don't need to ask for balance outside the loop because it's only stored if there's an account name
    balances.append(balance)
    name = input('What is the name of this account? ')

print('\nAccount Information:')
for i in range(len(account_names)):                                             #this lets me count from 0 to the size of the array
    print(f'{i}. {account_names[i]} = ${balances[i]:.2f}')
    sum += balances[i]
    if balances[i] > largest:                                                   #i'm not storing the largest value, i'm storing the index where it's saved. both would work though
        largest = i

print(f'\nTotal: ${sum:.2f}')
average = sum / (len(balances))
print(f'Average: ${average:.2f}')
print(f'Highest Balance: ${balances[largest]:.2f}')

update = input('\nDo you want to update an account? ')                          #asking for the first entry outside the loop prevents me from storing the exit 'key' in my list
while update.lower() == 'yes':
    sum = 0                                                                     #reset the sum or else it will keep getting higher and higher
    index = int(input('What account index do you want to update? '))
    new_balance = float(input('What is the new amount? '))
    balances[index] = new_balance                                               #stores the new balance in the index the user just gave

    print('\nAccount Information:')
    for i in range(len(account_names)):
        print(f'{i}. {account_names[i]} = ${balances[i]:.2f}')
        sum += balances[i]
        if balances[i] > largest:
            largest = i

    print(f'\nTotal: ${sum:.2f}')
    average = sum / (len(balances))
    print(f'Average: ${average:.2f}')
    print(f'Highest Balance: ${balances[largest]:.2f}')

    update = input('\nDo you want to update an account? ')