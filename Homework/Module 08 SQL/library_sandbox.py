import sqlite3


def run_first():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        country TEXT NOT NULL
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        year INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors(id) 
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS readers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        )""")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        reader_id INTEGER NOT NULL,
        loan_date TEXT NOT NULL,
        return_date DATE,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (reader_id) REFERENCES readers(id)
        )""")
        conn.commit()

        #Добавление авторов
        cursor.execute("""
        INSERT INTO authors (name, country)
        VALUES (?, ?)
        """, ('Лев Толстой', 'Россия'))

        cursor.execute("""
        INSERT INTO authors (name, country)
        VALUES (?, ?)
        """, ('Федор Достоевский', 'Россия'))

        cursor.execute("""
        INSERT INTO authors (name, country)
        VALUES (?, ?)
        """, ('Джордж Оруэлл', 'Великобритания'))
        conn.commit()

        #Добавление книг

        cursor.execute("""
        INSERT INTO books (title, author_id, year)
        VALUES (?,?,?)
        """, ('Война и мир', 1, 1869))

        cursor.execute("""
        INSERT INTO books (title, author_id, year)
        VALUES (?,?,?)
        """, ('Анна Каренина', 1, 1877))

        cursor.execute("""
        INSERT INTO books (title, author_id, year)
        VALUES (?,?,?)
        """, ('Преступление и наказание', 2, 1866))

        cursor.execute("""
        INSERT INTO books (title, author_id, year)
        VALUES (?,?,?)
        """, ('1984', 3, 1949))
        conn.commit()

        #Добавление читателей

        cursor.execute("""
        INSERT INTO readers (name)
        VALUES (?)
        """, ("Иван Иванов",))

        cursor.execute("""
        INSERT INTO readers (name)
        VALUES (?)
        """, ("Петр Петров",))
        conn.commit()

        #Добавление выдачи книг

        cursor.execute("""
        INSERT INTO loans (
        book_id, reader_id, loan_date, return_date)
        VALUES (?,?,?,?)
        """, (1, 1, '2026-09-16', None))

        cursor.execute("""
        INSERT INTO loans (
        book_id, reader_id, loan_date, return_date)
        VALUES (?,?,?,?)
        """,(4, 2, '2026-09-16', None))
        conn.commit()


def show_all_books():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * 
        FROM books
        """)
        
        rows = cursor.fetchall()  # ← Курьер забирает результаты
        for row in rows:
            print(f"ID: {row[0]}, Название: {row[1]}, Автор ID: {row[2]}, Год: {row[3]}")


def show_after_1900():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT title, year
        FROM books
        WHERE year > 1900
        """)
        
        rows = cursor.fetchall()  # ← Курьер забирает результаты
        print("\n=== Книги после 1900 года ===")
        for row in rows:
            print(f"{row[0]} ({row[1]})")


def show_title_author():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT books.title, authors.name
        FROM books
        JOIN authors ON authors.id = books.author_id
        """)
        
        rows = cursor.fetchall()  # ← Курьер забирает результаты
        print("\n=== Книги с авторами ===")
        for row in rows:
            print(f"'{row[0]}' написал {row[1]}")


def show_when():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT books.title, readers.name, loans.loan_date
        FROM books
        JOIN loans ON loans.book_id = books.id
        JOIN readers ON readers.id = loans.reader_id
        WHERE books.title = '1984'
        """)
        
        rows = cursor.fetchall()  # ← Курьер забирает результаты
        print("\n=== Кто взял '1984' ===")
        for row in rows:
            print(f"'{row[0]}' взял {row[1]} ({row[2]})")


show_all_books()
show_after_1900()
show_title_author()
show_when()