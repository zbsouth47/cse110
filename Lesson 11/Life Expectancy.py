"""
file: Life Expectancy.py
author: Zach Southwick

purpose: Sort data from a table of worldwide historical life expectancy data
"""
life_expectancies = []
life_expectancy = []
lowest = 200.00
lowest_country = ''
lowest_year = 0
highest = 0.00
highest_country = ''
highest_year = 0

with open("life-expectancy.csv") as life_expectancy_file:
    for line in life_expectancy_file:
        life_expectancy = line.strip().split(',')
        life_expectancies.append(life_expectancy)

life_expectancies.pop(0)

for line in life_expectancies:
    if float(line[3]) < lowest:
        lowest = float(line[3])
        lowest_country = line[0]
        lowest_year = int(line[2])
    if (float(line[3])) > highest:
        highest = float(line[3])
        highest_country = line[0]
        highest_year = int(line[2])

print(f'The lowest life expectancy on record is {lowest} for year {lowest_year} in country {lowest_country.title()}.')
print(f'The highest life expectancy on record is {highest} for year {highest_year} in country {highest_country.title()}.')

repeat = 'yes'
while repeat.lower() == 'yes':
    lowest = 200.00
    lowest_country = ''
    highest = 0.00
    highest_country = ''
    sum = 0
    count = 0
    average = 0

    interest_year = int(input('\nWhat year would you like to see life expectancy data for? '))
    for line in life_expectancies:
        if int(line[2]) == interest_year:
            sum += float(line[3])
            count += 1
            if float(line[3]) < lowest:
                lowest = float(line[3])
                lowest_country = line[0]
                lowest_year = int(line[2])
            if (float(line[3])) > highest:
                highest = float(line[3])
                highest_country = line[0]
                highest_year = int(line[2])

    print(f'\nFor the year {interest_year}: ')
    average = sum / count
    print(f'The average life expectancy across all countries is {average:.2f}')
    print(f'The lowest life expectancy is {lowest} in country {lowest_country.title()}.')
    print(f'The highest life expectancy is {highest} in country {highest_country.title()}.')
    repeat = input('\nWould you like to see another year (yes/no)? ')