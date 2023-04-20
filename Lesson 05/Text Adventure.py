"""
File: Text Adventure.py
Author: Zach Southwick

Purpose: To take the user through a text based adventure RPG
"""

choice = input('''You awake in a dim room lit only by the 
moonlight streaming in through a window high on the wall. 
Do you LOOK for the door or try to CLIMB something to the
window? ''')

if choice.lower() == 'look':
    choice = input('''You find the door and try it only to discover it 
    is locked and there's a keyhole on your side. Do you KNOCK or start 
    looking for a KEY? ''')
    if choice.lower() == 'knock':
        choice = input('''You knock several times, waiting for a response after
        each knock but no one answers. You start looking around the room and see
        a SAFE on the floor and a DESK against the wall. Which do you inspect first? ''')
        if choice.lower() == 'safe':
            choice = input('''The safe is small and has a 15 digit dial on it. There's also a 
            torn post-it note that reads 12-7- but the rest is torn away. Do you start TRYING 
            the combination or SEARCH for the rest of the note? ''')
            if choice.lower() == 'trying':
                last_digit = 0
                while last_digit != 9:
                    last_digit = int(input('What number do you try as the last digit of the combination? '))
                    if last_digit == 9:
                        print('''The combination 12-7-9 worked. The safe clicks open. A key is inside and you 
                        find that it works perfectly on the door. You are free!''')
                    else:
                        print('That didn\'t work, please try again')
            elif choice.lower() == 'search':
                choice = input('''text''')
        elif choice.lower() == 'desk':
            choice = input('''text''')
    elif choice.lower() == 'key':
        choice = input('''text''')
elif choice.lower() == 'climb':
        choice = input('''You notice a desk against the wall and start to
        drag it over. After your first pull, a piece of sticky note falls 
        to the floor. Do you KEEP dragging or PICK up the sticky note? ''')
else:
    print('That was not one of the possible answers. Please start over.')