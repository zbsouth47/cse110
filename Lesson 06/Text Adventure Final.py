"""
File: Text Adventure Final.py
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
torn post-it note that reads 12-7 but the rest is torn away. Do you start TRYING 
the combination or SEARCH for the rest of the note? ''')
            if choice.lower() == 'trying':
                last_digit = 0
                while last_digit != 9:
                    last_digit = int(input('What number do you try as the last digit of the combination? '))
                    if last_digit == 9:
                        print('''The combination 12-7-9 worked. The safe clicks open. A key is inside and you 
find that it works perfectly on the door. Congratulations, you are free!''')
                    else:
                        print('That didn\'t work, please try again ')
            elif choice.lower() == 'search':
                choice = input('''You start searching the desk and immediately spot the rest of the note. 
It has a -9 on it. You go back to the safe and try the combo 12-7-9. It opens and there's
a key inside. It works to unlock the door. Congratulations, you are free!''')
            else:
                print('That was not one of the possible answers. Please start over.')
        elif choice.lower() == 'desk':
            choice = input('''On the desk is a sticky note pad. The top sheet is torn but
the pen bled through to the next sheet. It has 12-7-9 written on it. You try this
on the safe and it opens to reveal a small key. The key works to unlock the door. 
Congratulations, you are free!''')
        else:
            print('That was not one of the possible answers. Please start over.')
    elif choice.lower() == 'key':
        choice = input('''You see a SAFE and DESK. Both seem like potential hiding places
for a key. Which do you try first? ''')
        if choice.lower() == 'safe':
            choice = input('''The safe is small and has a 15 digit dial on it. There's also a 
torn post-it note that reads 12-7 but the rest is torn away. Do you start TRYING 
the combination or SEARCH for the rest of the note? ''')
            if choice.lower() == 'trying':
                last_digit = 0
                while last_digit != 9:
                    last_digit = int(input('What number do you try as the last digit of the combination? '))
                    if last_digit == 9:
                        print('''The combination 12-7-9 worked. The safe clicks open. A key is inside and you 
find that it works perfectly on the door. Congratulations, you are free!''')
                    else:
                        print('That didn\'t work, please try again ')
            elif choice.lower() == 'search':
                choice = input('''You start searching the desk and immediately spot the rest of the note. 
It has a -9 on it. You go back to the safe and try the combo 12-7-9. It opens and there's
a key inside. It works to unlock the door. Congratulations, you are free!''')
            else:
                print('That was not one of the possible answers. Please start over.')
        elif choice.lower() == 'desk':
            choice = input('''On the desk is a sticky note pad. The top sheet is torn but
the pen bled through to the next sheet. It has 12-7-9 written on it. You try this
on the safe and it opens to reveal a small key. The key works to unlock the door. 
Congratulations, you are free!''')
        else:
            print('That was not one of the possible answers. Please start over.')
    else:
        print('That was not one of the possible answers. Please start over.')
elif choice.lower() == 'climb':
    choice = input('''You notice a broken chair but decide to use the desk against 
the wall instead. You start to drag it over. After your first heave, a piece of 
sticky note falls to the floor. Do you KEEP dragging or PICK up the sticky note? ''')
    if choice.lower() == 'keep':
        choice = input('''You drag the desk the rest of the way and climb up to the window.
The window is at ground level. It looks like you can break the glass. Do you SEARCH 
for something to break the glass or START searching the room? ''')
        if choice.lower() == 'search': 
            print('''You immediately spot the broken chair. One of the legs comes off
quite easily. You're able to easily break the glass with the metal foot of the chair
leg. Congratulations, you are free!''')
        elif choice.lower() == 'start':
            choice = input('''The torn piece of paper is the first thing you see. It's torn through
the middle and has a '-9' that was cut off from the rest of the paper. You spot a safe
as well. Do you go INSPECT the safe with the note you found or SEARCH the desk? ''')
            if choice.lower() == 'inspect':
                print('''You find that the rest of the sticky note is on the safe. You try the combination
'12-7-9' and it works. There is a key in the safe. The key works in the door and congratulations,
you are free!''')
            elif choice.lower() == 'search':
                print('''You find the sticky pad the note was written on. Even though the rest of the sheet is gone,
the writer's pen bled through and you can see the full note '12-7-9'. Thinking this might be the combo
to unlock the safe, you try it. You find a key in the safe that unlocks the door. Congratulations, you 
are free!''')
            else:
                print('That was not one of the possible answers. Please start over.')
        else:
            print('That was not one of the possible answers. Please start over.')
    elif choice.lower() == 'pick':
        choice = input('''The note is torn through the middle. It has a '-9' that was cut off
from the rest of the note. Do you search the DESK or the ROOM for the rest of the 
note? ''')
        if choice.lower() == 'desk':
            print('''The rest of the note is not on the desk but the sticky pad the note came from 
is. The writer's pen bled through the sticky note and you can see the digits 12-7-9. 
You try this on the safe. It opens to reveal a key. That key works on the door lock. 
Congratulations, you are free! ''')
        elif choice.lower() == 'room':
            print('''The only obvious thing left to check is the safe. On the safe is the first 
part of the sticky note 12-7. You put the whole combination into the safe dial. It 
opens and you find a key. That key works on the door. Congratulations, you are free!''')
        else:
            print('That was not one of the possible answers. Please start over.')
    else:
        print('That was not one of the possible answers. Please start over.')
else:
    print('That was not one of the possible answers. Please start over.')