# Login Attempt Limiter

This is a simple **Python Login System** that checks a username and password against stored credentials and limits the number of failed login attempts.

## 📌 Features

- Checks login credentials against stored values  
- Allows a maximum of 3 attempts  
- Displays remaining attempts after each failed try  
- Locks out the user after too many failed attempts  
- Uses a `while` loop and simple conditionals

## ⚙️ What’s Used

- **Input/Output:** `input()`, `print()`  
- **Comparison Operators:** `==`, `!=`  
- **Looping:** `while`  
- **Counters:** for tracking attempts  
- **Conditional Statements:** `if`, `else`

## 🚀 How to Run

1️⃣ Make sure you have Python installed.  
2️⃣ Save the script as `login_attempt_limiter.py`.  
3️⃣ Open your terminal, navigate to the project folder, and run:  
```bash
python login_attempt_limiter.py
```

## 💡 Example Output
```bash
.....LOGIN PAGE.....

Enter username: user1
Enter password: 1234
Welcome, user1!

.....LOGIN PAGE.....

Enter username: wronguser
Enter password: 0000
Invalid username or password. 2 attempts left.

.....LOGIN PAGE.....

Enter username: wronguser
Enter password: 0000
Invalid username or password. 1 attempts left.

.....LOGIN PAGE.....

Enter username: wronguser
Enter password: 0000
Too many failed attempts. Try again later.
```
