age1 = int(input('What is the age of the first rider? '))
if age1 >= 12 and age1 <= 17:
    golden_ticket = input('Do you have a golden passport (y/n)? ')
    if golden_ticket.lower() == 'y':
        age1 = 18
height1 = int(input('What is the height of the first rider? '))
rider2 = input('Is there a second rider (yes/no)? ')

if rider2.lower() == 'no':
    if height1 >= 62 and age1 >= 18:
        ride_decision = True
    else:
        ride_decision = False
else:
    age2 = int(input('What is the age of the second rider? '))
    if age2 >= 12 and age2 <= 17:
        golden_ticket = input('Do you have a golden passport (y/n)? ')
        if golden_ticket.lower() == 'y':
            age2 = 18
    height2 = int(input('What is the height of the second rider? '))
    
    if height1 < 36 or height2 < 36:
        ride_decision = False
    else:
        if age1 >= 18 or age2 >= 18:
            ride_decision = True
        else:
            if age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
                ride_decision = True
            elif (age1 >= 16 and age2 >= 14) or (age2 >= 16 and age1 >= 14):
                ride_decision = True
            else:
                ride_decision = False

if ride_decision:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')