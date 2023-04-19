"""
file: People List.py
author: Zach Southwick

purpose: Sort through a list of people
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

persons = []
youngest = 200
youngest_name = ''

for p in people: 
    person = p.strip().split(' ')
    persons.append(person)

for p in persons:
    print(f'This person\'s name is {p[0]} and they are {p[1]} years old.')
    if int(p[1]) < youngest:
        youngest = int(p[1])
        youngest_name = p[0]

print(f'\nThe youngest person is {youngest_name} at {youngest} years old.')