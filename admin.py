def admin_menu(conn):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            if title and author and year.isdigit():
                add_book(conn, title, author, int(year))
                print("Book added successfully.")
            else:
                print("Invalid input. Please enter valid book details.")
        elif choice == '2':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new publication year: ")
            if title and author and year.isdigit():
                update_book(conn, book_id, title, author, int(year))
                print("Book updated successfully.")
            else:
                print("Invalid input. Please enter valid book details.")
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(conn, book_id)
            print("Book deleted successfully.")
        elif choice == '4':
            title = input("Enter book title to search: ")
            books = search_books(conn, title)
            for book in books:
                print(book)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(conn, title, author, year):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()

def update_book(conn, book_id, title, author, year):
    cursor = conn.cursor()
    cursor.execute("UPDATE Books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, book_id))
    conn.commit()

def delete_book(conn, book_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE id = ?", (book_id,))
    conn.commit()

def search_books(conn, title):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books WHERE title LIKE ?", ('%' + title + '%',))
    return cursor.fetchall()
