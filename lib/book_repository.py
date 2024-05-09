from lib.book import *

class BookRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            book = Book(row["id"], row["title"], row["author_name"])
            books.append(book)
        return books
