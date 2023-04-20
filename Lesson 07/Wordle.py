"""
File: Wordle.py
Author: Zach Southwick

Purpose: Let the user play a game of wordle. 
"""
import random

#word_pool = open("word_list.txt").read().split()
#magic_word = random.choice(word_pool)

word_pool = ['fun', 'jump', 'crazy', 'faster', 'picture', 'creation']
rand_word = random.randint(0, 5)
magic_word = word_pool[rand_word]

magic_word_list = list(magic_word)
size_of_word = len(magic_word_list)
solution = list()
for i in range(size_of_word):
    solution.append('_')

guess = ''
guess_list = list()
count = 0

#print(f'{magic_word}')                                   #**delete or comment out before submitting**

while guess.lower() != magic_word:
    solution_string = ' '.join(solution)
    print(f'Your hint is: {solution_string}')
    guess = input('What is your guess? ')
    guess_list = list(guess.lower())
    if len(guess_list) != size_of_word:
        print('Sorry, the guess must have the same number of letters as the secret word. \n')
    else:
        for i in range(size_of_word):
            guess_letter = guess_list[i]
            magic_word_letter = magic_word_list[i]
            if guess_letter == magic_word_letter:
                solution[i] = guess_letter.capitalize()
            elif guess_letter in magic_word:
                solution[i] = guess_letter.lower()
            else:
                solution[i] = '_' 
    count += 1

print('\nCongratulations! You solved it!')
print(f'It took you {count} guesses.')