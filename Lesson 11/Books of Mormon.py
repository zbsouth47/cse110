"""
file: Books of Mormon.py
author: Zach Southwick

purpose: Divide up a file provided to me and display its contents
"""
with open("books.txt") as books:
    for book in books:
        print(book, end='')