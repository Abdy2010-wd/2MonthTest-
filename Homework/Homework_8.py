import sqlite3


def create_tables():
    """Пересоздаёт таблицы books и genres"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Удаляем старые таблицы
    cursor.execute("DROP TABLE IF EXISTS books")
    cursor.execute("DROP TABLE IF EXISTS genres")

    # Создаём таблицу жанров
    cursor.execute("""
    CREATE TABLE genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    # Создаём таблицу книг
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
    """Добавляет книги"""
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Получаем id жанров в словарь
    cursor.execute("SELECT id, name FROM genres")
    genres_dict = {name: genre_id for genre_id, name in cursor.fetchall()}


