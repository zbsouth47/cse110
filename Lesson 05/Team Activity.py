grade = float(input('What is your grade percentage? '))
letter_grade = ''
sign = ''

if grade >=  90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

last_digit = grade % 10

if last_digit >= 7 and letter_grade != 'A' and letter_grade != 'F':
    sign = '+'
elif last_digit <= 3 and letter_grade != 'F':
    sign = '-'

print(f'Your grade is {letter_grade}{sign}.')
if grade >= 70:
    print('Congratulations! You passed the class!')
else:
    print('Sorry, you didn\'t pass. Better luck next semester!')