# Student Management System

This is a simple **Python Student Management System** that lets you add, update, remove, search, and display student names using a list, `while` loop, and modern `match case` syntax.

## 📌 Features

- Add new student names to the list  
- Update a student’s name by index  
- Remove a student by name  
- Search if a student exists in the list  
- Display all students with their index  
- Input validation for index and empty list checks  
- Uses `match case` (Python 3.10+)

## ⚙️ What’s Used

- **List:** to store student names  
- **Looping:** `while True`  
- **Pattern Matching:** `match case` (Python 3.10+)  
- **Input/Output:** `input()`, `print()`  
- **Type Conversion:** `int()`  
- **Conditional Statements:** `if`, `else`  
- **Exception Handling:** `try/except` for safe index input  
- **Break Statement:** `break`

## 🚀 How to Run

1️⃣ Make sure you have **Python 3.10 or higher** installed.  
2️⃣ Save the script as `student_management_system.py`.  
3️⃣ Open your terminal, navigate to the project folder, and run:  
```bash
python student_management_system.py
```
## 💡 Example Output
```bash
Student Management System

1. Add a Student
2. Update a Student name
3. Remove a Student
4. Search for a Student
5. Show all Students
6. Exit the Program

Enter your choice: 1
Enter the name to Add: Alex
Alex added to the list.

Enter your choice: 5

List of Students:
0 -> Alex

Enter your choice: 2
Enter the index you want to Update: 0
Enter the new name: Alice
Alice updated at index 0

Enter your choice: 4
Enter the name to Search: Alice
Alice is in the list.

Enter your choice: 3
Enter the name to Remove: Alice
Alice removed from the list.

Enter your choice: 6
Exited from Program.
```
