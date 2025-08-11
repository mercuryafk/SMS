import tkinter as tk
from tkinter import messagebox, ttk
import backend

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System - Login")
        self.root.geometry("400x350")
        backend.create_table()

        self.build_login_screen()

    def build_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Username:").pack(pady=(20,5))
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        tk.Label(self.root, text="Password:").pack(pady=(10,5))
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=15)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if backend.authenticate(username, password):
            self.build_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def build_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.title("Student Management System")

        tk.Label(self.root, text="Student Management System", font=("Ubuntu", 14)).pack(pady=10)
        tk.Label(self.root, text="by Umesh K").pack(pady=(10))

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Student", width=15, command=self.add_student_dialog).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="View Students", width=15, command=self.view_students_dialog).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Update Student", width=15, command=self.update_student_dialog).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Delete Student", width=15, command=self.delete_student_dialog).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Logout", width=10, command=self.logout).pack(pady=10)

    def add_student_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Student")

        tk.Label(dialog, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(dialog)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Age:").grid(row=1, column=0, padx=10, pady=5)
        entry_age = tk.Entry(dialog)
        entry_age.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(dialog, text="Course:").grid(row=2, column=0, padx=10, pady=5)
        entry_course = tk.Entry(dialog)
        entry_course.grid(row=2, column=1, padx=10, pady=5)

        def add_student():
            name = entry_name.get().strip()
            age = entry_age.get().strip()
            course = entry_course.get().strip()

            # Basic empty/age validation in frontend
            if not name or not age.isdigit() or not course:
                messagebox.showerror("Input Error", "Please enter valid data.")
                return

            # Call backend and capture the result
            result = backend.add_student(name, int(age), course)

            # If backend returns error string, show error popup
            if isinstance(result, str) and result.startswith("Error:"):
                messagebox.showerror("Backend Error", result)
                return

            # Otherwise success
            messagebox.showinfo("Success", f"Student '{name}' added.")
            dialog.destroy()

        tk.Button(dialog, text="Add", command=add_student).grid(row=3, column=0, columnspan=2, pady=10)

    def view_students_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("View Students")
        dialog.geometry("800x300")

        columns = ("ID", "Name", "Age", "Course")
        tree = ttk.Treeview(dialog, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        tree.pack(fill="both", expand=True)

        # Clear existing rows if any (just in case)
        for row in tree.get_children():
            tree.delete(row)

        for student in backend.view_students():
            tree.insert("", "end", values=student)

    def update_student_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Student")

        tk.Label(dialog, text="Student ID:").grid(row=0, column=0, padx=10, pady=5)
        entry_id = tk.Entry(dialog)
        entry_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(dialog, text="New Name:").grid(row=1, column=0, padx=10, pady=5)
        entry_name = tk.Entry(dialog)
        entry_name.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(dialog, text="New Age:").grid(row=2, column=0, padx=10, pady=5)
        entry_age = tk.Entry(dialog)
        entry_age.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(dialog, text="New Course:").grid(row=3, column=0, padx=10, pady=5)
        entry_course = tk.Entry(dialog)
        entry_course.grid(row=3, column=1, padx=10, pady=5)

        def update_student():
            student_id = entry_id.get().strip()
            name = entry_name.get().strip()
            age = entry_age.get().strip()
            course = entry_course.get().strip()

            if not student_id.isdigit():
                messagebox.showerror("Input Error", "Student ID must be a number.")
                return
            if not name or not age.isdigit() or not course:
                messagebox.showerror("Input Error", "Please enter valid data.")
                return

                # Call backend and capture the result
            result = backend.update_student(int(student_id), name, int(age), course)

            # If backend returns error string, show error popup
            if isinstance(result, str) and result.startswith("Error:"):
                messagebox.showerror("Backend Error", result)
                return

            messagebox.showinfo("Success", "Student updated successfully.")
            dialog.destroy()

        tk.Button(dialog, text="Update", command=update_student).grid(row=4, column=0, columnspan=2, pady=10)

    def delete_student_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Delete Student")

        tk.Label(dialog, text="Student ID:").pack(padx=10, pady=10)
        entry_id = tk.Entry(dialog)
        entry_id.pack(padx=10, pady=5)

        def delete_student():
            student_id = entry_id.get().strip()
            if not student_id.isdigit():
                messagebox.showerror("Input Error", "Student ID must be a number.")
                return
            backend.delete_student(int(student_id))
            messagebox.showinfo("Success", "Student deleted successfully.")
            dialog.destroy()

        tk.Button(dialog, text="Delete", command=delete_student).pack(pady=10)

    def logout(self):
        self.root.title("Student Management System - Login")
        self.root.geometry("400x350")
        self.build_login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()