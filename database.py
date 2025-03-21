import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def setup_database(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        contact_info TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Issued_Books (
                        id INTEGER PRIMARY KEY,
                        book_id INTEGER,
                        user_id INTEGER,
                        issue_date TEXT,
                        return_date TEXT,
                        FOREIGN KEY (book_id) REFERENCES Books (id),
                        FOREIGN KEY (user_id) REFERENCES Users (id)
                    )''')
    conn.commit()
