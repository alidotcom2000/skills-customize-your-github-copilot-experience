import sqlite3

DATABASE_NAME = "books.db"


def get_connection():
    """Return a connection to the catalog database."""
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """Create the books table if it does not exist yet."""
    pass


def add_book(title, author, year):
    """Insert a book and return its new ID."""
    pass


def list_books():
    """Return all books ordered by title."""
    pass


def search_books(search_text):
    """Return books whose title or author contains search_text."""
    pass


def set_reading_status(book_id, is_read):
    """Update a book's reading status and return whether it changed."""
    pass


def delete_book(book_id):
    """Delete a book and return whether it existed."""
    pass


def display_books(books):
    """Print books in a readable format."""
    if not books:
        print("No books found.")
        return

    for book in books:
        book_id, title, author, year, is_read = book
        status = "Read" if is_read else "Unread"
        print(f"[{book_id}] {title} by {author} ({year}) - {status}")


def main():
    create_table()
    print("Book Catalog")
    print("Complete the functions above, then add a menu here to try them.")


if __name__ == "__main__":
    main()
