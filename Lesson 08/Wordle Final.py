"""
File: Wordle Final.py
Author: Zach Southwick

Purpose: Let the user play a game of wordle. 
"""

import random
choice = 'yes'

while choice == 'yes':
    word_pool = open("word_list.txt").read().split()
    magic_word = random.choice(word_pool)

    #word_pool = ['fun', 'jump', 'crazy', 'faster', 'picture', 'creation']  #commented out since I got the file working 
    #rand_word = random.randint(0, 5)                                       #but I didn't want to lose this information
    #magic_word = word_pool[rand_word]

    magic_word_list = list(magic_word)
    size_of_word = len(magic_word_list)
    alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    solution = list()
    for i in range(size_of_word):
        solution.append('_')

    guess = ''
    guess_list = list()
    count = 0

    while guess.lower() != magic_word:
        solution_string = ' '.join(solution)
        print(f'Your hint is: {solution_string}\n')
        for i, letter in enumerate(alphabet):
            if i == 9:
                print(letter + '\n' + ' ', end='')
            elif i == 18:
                print(letter + '\n' + '  ', end='')
            else:
                print(letter + ' ', end='')
        guess = input('\n\nWhat is your guess? ')
        guess_list = list(guess.lower())
        if len(guess_list) != size_of_word:
            print('Sorry, the guess must have the same number of letters as the secret word. \n')
        else:
            for i in range(size_of_word):
                guess_letter = guess_list[i]
                magic_word_letter = magic_word_list[i]
                if guess_letter == magic_word_letter:
                    solution[i] = guess_letter.capitalize()
                    for i, letter in enumerate(alphabet):
                        if letter == guess_letter:
                            alphabet[i] = guess_letter.capitalize()
                elif guess_letter in magic_word:
                    solution[i] = guess_letter.lower()
                    for i, letter in enumerate(alphabet):
                        if letter == guess_letter:
                            alphabet[i] = guess_letter.capitalize()
                else:
                    solution[i] = '_' 
                    for i, letter in enumerate(alphabet):
                        if letter == guess_letter:
                            alphabet[i] = '_'
        count += 1

    print('\nCongratulations! You solved it!')
    print(f'It took you {count} guesses.')
    choice = input('Would you like to play again (yes/no)? ')

print('Thanks for playing!')