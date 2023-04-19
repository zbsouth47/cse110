books = []                                                  #if I declare my list outside of the file read, I can keep using it after the file has closed
biggest = 0                                                 #initializing varialbe for most chapters
biggest_book = ''                                           #initializing variable for biggest book

with open("books_and_chapters.txt") as f:
    for line in f:
        book = line.strip().split(':')                      #store the list from the line into a new variable
        books.append(book)                                  #append that list to my big list declared earlier

scripture = input('Which book of scripture would you like to learn about (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price)? ')
print()                                                     #^which book of scripture are we basing this on?
for book in books:
    book_of_scripture = book[2]                             #book of scripture is in the third spot
    book_title = book[0]                                    #actual book is in the first spot
    num_chapters = int(book[1])                             #number of chapters is in the second spot
    if book_of_scripture.lower() == scripture.lower():      #if the scipture in the list we're in is the same as the scripture of interest, start checking things
        print(f'Scripture: {book_of_scripture}, Book: {book_title}, Chapters: {num_chapters}')
        if num_chapters > biggest:
            biggest = num_chapters                          #start checking for biggest and store biggest book + number of chapters
            biggest_book = book_title

print(f'\nThe biggest book in {scripture.title()} is {biggest_book} and it has {biggest} chapters.')