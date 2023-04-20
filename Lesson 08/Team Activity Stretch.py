quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'
quote_list = list(quote)
choice = 'yes'

while choice == 'yes':
    number = int(input('Please enter a number: '))
    for i, letter in enumerate(quote_list):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    choice = input('\nWould you like to enter another number (yes/no)? ')

print('Goodbye')