import sqlite3

# -----------------------------
# Database setup (runs once)
# -----------------------------
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

# -----------------------------
# Add a new student
# -----------------------------
def add_student():
    name = input("Enter student name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not name or not course or not age.isdigit():
        print("❌ Invalid input. Please try again.")
        return

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, int(age), course))
    conn.commit()
    conn.close()
    print(f"✅ Student '{name}' added successfully!")

# -----------------------------
# Update student
# -----------------------------
def update_student():
    student_id = input("Enter student ID to update: ")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
        return

    print(f"Current details - Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")
    name = input("Enter new name (leave blank to keep current): ") or student[1]
    age = input("Enter new age (leave blank to keep current): ") or student[2]
    course = input("Enter new grade (leave blank to keep current): ") or student[3]

    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    conn.commit()
    print("Student updated successfully!")

# -----------------------------
# delete student
# -----------------------------
def delete_student():
    student_id = input("Enter student ID to delete: ")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
        return

    confirm = input(f"Are you sure you want to delete {student[1]}? (y/n): ").lower()
    if confirm == "y":
        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        conn.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


# -----------------------------
# Main Menu
# -----------------------------
def menu():
    while True:
        print("\n📌 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Students")
        print("4. Delete Students")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    init_db()
    menu()
