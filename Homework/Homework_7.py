import sqlite3

def create_table():
 """Создаёт таблицу books"""
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS books ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    author TEXT,
    publication_year INTEGER,
    genre TEXT, 
    number_of_pages INTEGER, 
    number_of_copies INTEGER 
)
""")

conn.commit()
conn.close()


def insert_books():
 """Добавляет в таблицу минимум 10 книг"""
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

books = [ ("Преступление и наказание", "Ф. М. Достоевский", 1866, "Роман", 672, 5),
          ("Война и мир", "Л. Н. Толстой", 1869, "Роман", 1274, 3),
          ("Анна Каренина", "Л. Н. Толстой", 1877, "Роман", 864, 4),
          ("Евгений Онегин", "А. С. Пушкин", 1833, "Роман в стихах", 384, 6),
          ("Мастер и Маргарита", "М. А. Булгаков", 1967, "Роман", 512, 7),
          ("Отцы и дети", "И. С. Тургенев", 1862, "Роман", 320, 5),
          ("Идиот", "Ф. М. Достоевский", 1869, "Роман", 640, 2),
          ("Доктор Живаго", "Б. Л. Пастернак", 1957, "Роман", 704, 4),
          ("Герой нашего времени", "М. Ю. Лермонтов", 1840, "Роман", 352, 3),
          ("Чайка", "А. П. Чехов", 1896, "Пьеса", 120, 8) ]

cursor.executemany("""
            INSERT INTO books (name, author, publication_year, genre, 
            number_of_pages, number_of_copies) 
            VALUES (?, ?, ?, ?, ?, ?) """, books)

conn.commit()
conn.close()

def delete_book(book_name):
 """Удаляет книгу по названию"""
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM books WHERE name = ?",
(books,))

conn.commit()
conn.close()

if __name__ == "__main__":
    create_table()
    insert_books()