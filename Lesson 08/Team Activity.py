word = 'commitment'
#word_list = list(word)

fav_letter = input('What is your favorite letter? ')

for letter in word:
    if letter == fav_letter.lower():
        #print('_', end="")
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")

