def user_menu(conn):
    while True:
        print("\nUser Menu:")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. View Issued Books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = int(input("Enter book ID to issue: "))
            user_id = int(input("Enter your user ID: "))
            issue_date = input("Enter issue date (YYYY-MM-DD): ")
            issue_book(conn, book_id, user_id, issue_date)
            print("Book issued successfully.")
        elif choice == '2':
            issued_book_id = int(input("Enter issued book ID to return: "))
            return_date = input("Enter return date (YYYY-MM-DD): ")
            return_book(conn, issued_book_id, return_date)
            print("Book returned successfully.")
        elif choice == '3':
            user_id = int(input("Enter your user ID: "))
            issued_books = view_issued_books(conn, user_id)
            for book in issued_books:
                print(book)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def issue_book(conn, book_id, user_id, issue_date):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Issued_Books (book_id, user_id, issue_date) VALUES (?, ?, ?)", (book_id, user_id, issue_date))
    conn.commit()

def return_book(conn, issued_book_id, return_date):
    cursor = conn.cursor()
    cursor.execute("UPDATE Issued_Books SET return_date = ? WHERE id = ?", (return_date, issued_book_id))
    conn.commit()

def view_issued_books(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Issued_Books WHERE user_id = ?", (user_id,))
    return cursor.fetchall()
