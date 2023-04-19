def display_regular(user_string):
    print(user_string)

def display_uppercase(user_string):
    print(user_string.upper())

def display_lowercase(user_string):
    print(user_string.lower())

user_message = input('What is your message? ')

display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)