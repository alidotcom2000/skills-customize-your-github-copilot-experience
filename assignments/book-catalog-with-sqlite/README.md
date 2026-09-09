# 📘 Assignment: Book Catalog with SQLite

## 🎯 Objective

Build a command-line book catalog that stores data in a SQLite database. You will practice database tables, SQL queries, Python functions, and persistent data that remains available after your program closes.

## 📝 Tasks

### 🛠️ Create the Database and Books Table

#### Description

Complete the database setup function so the program creates a SQLite database file and a `books` table when it starts. The table should store each book's title, author, publication year, and reading status.

#### Requirements

Completed program should:

- Connect to a SQLite database named `books.db`
- Create a `books` table if it does not already exist
- Use an integer primary key named `id`
- Store `title`, `author`, `year`, and `is_read` values with appropriate SQLite types
- Close the database connection when each operation is complete

### 🛠️ Add and List Books

#### Description

Implement functions that add a book to the catalog and display all saved books in a readable format. Run the program more than once to confirm that the data persists.

#### Requirements

Completed program should:

- Insert a new book using a parameterized SQL query
- Return or display the ID assigned to the new book
- Retrieve all books ordered by title
- Display each book's title, author, publication year, and reading status
- Keep user input separate from SQL statements by using query parameters

### 🛠️ Search and Update Books

#### Description

Add a search feature and a way to mark a book as read or unread. Searching should work with part of a title or author name.

#### Requirements

Completed program should:

- Search titles and authors using a case-insensitive partial match
- Display a helpful message when no books match
- Update the reading status for a selected book ID
- Handle an ID that does not exist without crashing
- Confirm whether an update succeeded

### 🛠️ Add Validation and Delete Support

#### Description

Make the catalog safer and more complete by validating book details and allowing users to remove a book. This task is a stretch goal for students who finish the core catalog early.

#### Requirements

Completed program should:

- Reject blank titles and author names
- Validate that the publication year is a reasonable integer
- Delete a book by ID only after confirming the book exists
- Handle invalid menu choices and non-numeric IDs gracefully
- Include a short example session or comments explaining how the catalog works
