from lib.book import *

'''
Constructs with
id, title, author_name
'''
def test_constructs_with_fields():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

'''
When i construct two Books with the same fields
They are equal
'''
def test_equality():
    book_1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book_2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book_1 == book_2

'''
When i construct a Book
and i format it to a string
then it comes out in a friendly format
'''

def test_formatting():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "Book(1, Nineteen Eighty-Four, George Orwell)"