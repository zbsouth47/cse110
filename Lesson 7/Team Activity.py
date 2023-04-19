import random

again = 'yes'

while again == 'yes':
    number = random.randint(1, 100)
    count = 1

    guess = int(input('What is your guess? '))

    while guess != number:
        if guess > number:
            print('Lower')
        else:
            print('Higher')
        count += 1
        guess = int(input('What is your guess? '))

    print('You guessed it!')
    print(f'It took you {count} tries.')
    again = input('Would you like to play again (yes/no)? ')