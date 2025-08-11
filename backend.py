import sqlite3
import re

DB_NAME = "studentsx.db"

# Hardcoded valid credentials (for learning)
VALID_USERNAME = "admin"
VALID_PASSWORD = "123"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS studentsx (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def authenticate(username, password):
    """
    Simple authentication function.
    Returns True if username/password match the hardcoded values, else False.
    """
    return username == VALID_USERNAME and password == VALID_PASSWORD

def add_student(name, age, course):
    # Name validation: only letters and spaces
    if not re.match(r'^[A-Za-z ]+$', name):
        return "Error: Name must only contain letters and spaces."
    if not re.match(r'^[A-Za-z ]+$', course):
        return "Error: Course must only contain letters and spaces."
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO studentsx (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM studentsx")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(student_id, name, age, course):
    if not re.match(r'^[A-Za-z ]+$', name):
        return "Error: Name must only contain letters and spaces."
    if not re.match(r'^[A-Za-z ]+$', course):
        return "Error: Course must only contain letters and spaces."
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE studentsx SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM studentsx WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
