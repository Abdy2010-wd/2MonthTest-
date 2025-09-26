import


def create_tables():
    conn.execute("""CREATE TABLE EXISTS students (
    name TEXT,
    age INTEGER,
    city TEXT
    )
""")

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

