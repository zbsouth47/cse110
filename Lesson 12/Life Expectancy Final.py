"""
file: Life Expectancy Final.py
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
    lowest_year = 0
    highest = 0.00
    highest_country = ''
    highest_year = 0
    sum = 0
    count = 0
    average = 0


    which_value = input('Would you prefer to see data based on YEAR or COUNTRY? ')
    if which_value.lower() == 'year':
        interest_year = int(input('\nWhat year would you like to see life expectancy data for? '))
        for line in life_expectancies:
            if int(line[2]) == interest_year:
                sum += float(line[3])
                count += 1
                if float(line[3]) < lowest:
                    lowest = float(line[3])
                    lowest_country = line[0]
                if (float(line[3])) > highest:
                    highest = float(line[3])
                    highest_country = line[0]
        if sum != 0:
            print(f'\nFor the year {interest_year}: ')
            average = sum / count
            print(f'The average life expectancy across all countries is {average:.2f}')
            print(f'The lowest life expectancy is {lowest} in country {lowest_country.title()}.')
            print(f'The highest life expectancy is {highest} in country {highest_country.title()}.')
        else:
            print('That is not a valid year. Please try again.')
    elif which_value.lower() == 'country':
        interest_country = input('\nWhat country would you like to see life expectancy data for? ')
        for line in life_expectancies:
            if line[0].lower() == interest_country.lower():
                sum += float(line[3])
                count += 1
                if float(line[3]) < lowest:
                    lowest = float(line[3])
                    lowest_year = int(line[2])
                if (float(line[3])) > highest:
                    highest = float(line[3])
                    highest_year = int(line[2])
        if sum != 0:
            print(f'\nFor the country {interest_country.title()}: ')
            average = sum / count
            print(f'The average life expectancy for {interest_country.title()} is {average:.2f}')
            print(f'The lowest life expectancy is {lowest} in year {lowest_year}.')
            print(f'The highest life expectancy is {highest} in year {highest_year}.')
        else: 
            print('That is not a valid country. Please try again.')
    else:
        print('That is not a valid option. Please try again.')
    
    repeat = input('\nWould you like to see another year/country (yes/no)? ')