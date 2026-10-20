import sqlite3

conn = sqlite3.connect("just.db")
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
""")


cur.execute(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    ("John", 25)
)


conn.commit()


cur.execute("SELECT * FROM users")
rows = cur.fetchall()

# Display results
for row in rows:
    print(row)

# Close the connection
conn.close()
