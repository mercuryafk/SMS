# Student Management System

A simple Python-based Student Management System demonstrating basic CRUD operations with a SQLite database, wrapped in a user-friendly Tkinter GUI.  

---

## Features

- User authentication (hardcoded username and password)  
- Add, view, update, and delete student records  
- Simple and intuitive graphical interface using Tkinter  
- Backend and frontend code modularized for easy maintenance

---

## Getting Started

### Prerequisites

- Python 3.x  
- Tkinter (usually included with Python)  
- SQLite (built-in with Python)  

### Setup

1. Download ```gui.exe``` from the repository (on windows, mac app coming soon!)

2. Run the GUI application!

## Usage

### Login

**Username**: 
```
admin
```

**Password**: 
```
123
```

```
Note:
The username and password are hardcoded for learning purposes, please use them for logging in the app.
```

## Main Application


Once logged in, you can:




1. **Add Student**: Enter name, age, and course details in a popup form.

2. **View Students**: See a table of all student records with ID, Name, Age, and Course columns.

3. **Update Student**: Modify existing student information by entering the student ID and new details.

4. **Delete Student**: Remove a student record by entering the student ID.

5. Use the **Logout** button to return to the login screen.




## Code Structure

- **backend.py**:  Handles database creation, user authentication, and all CRUD operations with SQLite.

- **gui.py**:  Implements the Tkinter GUI, connects user interactions to backend functions.





## Future Improvements


- Replace hardcoded credentials with database-stored users and password hashing.

- Add user registration and password recovery.

- Improve GUI styling and usability.

- Add data export/import features.



## License


This project is for educational purposes and free to use.

---

Feel free to open issues or contribute improvements!

