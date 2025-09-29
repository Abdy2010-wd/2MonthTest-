import sqlite3


def create_tables():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("DROP TABLE IF EXISTS genres")

    cursor.execute("""
    CREATE TABLE genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER,
        number_of_pages INTEGER,
        number_of_copies INTEGER,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genres (id)
    )
    """)

    conn.commit()
    conn.close()


def insert_genres():
    """Добавляет жанры"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    genres = [
        ("Роман",),
        ("Пьеса",),
        ("Поэма",),
        ("Фантастика",)
    ]

    cursor.executemany("INSERT INTO genres (name) VALUES (?)", genres)

    conn.commit()
    conn.close()


def insert_books():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM genres")
    genres_dict = {name: genre_id for genre_id, name in cursor.fetchall()}

    books = [
        ("Преступление и наказание", "Ф. М. Достоевский", 1866, 672, 5, genres_dict["Роман"]),
        ("Война и мир", "Л. Н. Толстой", 1869, 1274, 3, genres_dict["Роман"]),
        ("Анна Каренина", "Л. Н. Толстой", 1877, 864, 4, genres_dict["Роман"]),
        ("Евгений Онегин", "А. С. Пушкин", 1833, 384, 6, genres_dict["Поэма"]),
        ("Мастер и Маргарита", "М. А. Булгаков", 1967, 512, 7, genres_dict["Фантастика"]),
        ("Отцы и дети", "И. С. Тургенев", 1862, 320, 5, genres_dict["Роман"]),
        ("Идиот", "Ф. М. Достоевский", 1869, 640, 2, genres_dict["Роман"]),
        ("Доктор Живаго", "Б. Л. Пастернак", 1957, 704, 4, genres_dict["Роман"]),
        ("Герой нашего времени", "М. Ю. Лермонтов", 1840, 352, 3, genres_dict["Роман"]),
        ("Чайка", "А. П. Чехов", 1896, 120, 8, genres_dict["Пьеса"]),
    ]

    cursor.executemany("""
    INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


def get_all_books():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT books.id, books.name, books.author, genres.name AS genre
    FROM books
    JOIN genres ON books.genre_id = genres.id
    ORDER BY books.id
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    create_tables()
    insert_genres()
    insert_books()

    books = get_all_books()
    for book in books:
        print(book)
