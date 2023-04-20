numbers = []
sum = 0
largest = -214748647                              #smallest possible value that an int can hold
smallest = 214748647                              #largest possible value that an int can hold

print('Enter a list of numbers, type 0 when finished.')

number = int(input('Enter number: '))             #asking for the first entry outside the loop prevents me from storing the exit 'key' in my list
while number != 0:
    numbers.append(number)
    number = int(input('Enter number: '))

for num in numbers:
    sum += num                                    #sums the numbers in the list
    if num > largest:                             #if the current number is larger than the current largest, it becomes the new largest
        largest = num
    if num > 0:                                   #if the current number is positive, it checks if it's smaller than the current smallest
        if num < smallest:
            smallest = num

print(f'\nThe sum is: {sum}')

average = sum / (len(numbers))                    #computes the average
print(f'The average is: {average}')

print(f'The largest number is: {largest}')

if smallest == 214748647:                         #checks if smallest has changed at all, if it hasn't, they didn't enter a positive number
    print('The smallest positive number is: You never entered a postive number!')
else:
    print(f'The smallest postive number is: {smallest}')

numbers.sort()                                    #I didn't have to include a library for this, VS Code interpreted it as a default function
print('\nThe sorted list is: ')
for num in numbers:
    print(num)