import sqlite3
from database import create_connection, setup_database
from admin import admin_menu
from user import user_menu

def main():
    conn = create_connection("library.db")
    setup_database(conn)
    
    print("Welcome to the Library Management System")
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            admin_menu(conn)  # Call to admin_menu for admin functionalities
        elif choice == '2':
            user_menu(conn)  # Call to user_menu for user functionalities
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()
