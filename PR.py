class Book:
    def __init__(self, title, author, genre, publication_year, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.isbn = isbn
        self.reading_progress = None
        self.lent_to = None
        self.due_date = None

class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre, publication_year, isbn):
        book = Book(title, author, genre, publication_year, isbn)
        self.books.append(book)

    def log_reading_progress(self, title, current_page, start_date, completion_date=None):
        for book in self.books:
            if book.title == title:
                book.reading_progress = {
                    "current_page": current_page,
                    "start_date": start_date,
                    "completion_date": completion_date
                }
                break

    def lend_book(self, title, lent_to, due_date):
        for book in self.books:
            if book.title == title:
                book.lent_to = lent_to
                book.due_date = due_date
                break

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    def get_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.reading_progress and book.reading_progress["completion_date"])
        return {
            "total_books": total_books,
            "read_books": read_books,
            "currently_reading": total_books - read_books
        }

# Example usage
library = LibraryManager()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, "9780743273565")
library.add_book("1984", "George Orwell", "Dystopian", 1949, "9780451524935")

library.log_reading_progress("The Great Gatsby", current_page=50, start_date="2023-10-01", completion_date="2023-10-10")
library.lend_book("1984", lent_to="John Doe", due_date="2023-11-01")

# Searching for books
search_results = library.search_books("1984")
print("Search Results:", [book.title for book in search_results])

# Getting statistics
stats = library.get_statistics()
print("Library Statistics:", stats)