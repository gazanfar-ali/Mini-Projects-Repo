# Password Checker

This is a simple **Python Password Checker** that verifies a user’s input against a stored password with limited attempts and an option to exit early.


## 📌 Features

- Checks password against a stored value  
- Allows up to 3 attempts  
- Displays remaining attempts after each failed try  
- Allows the user to exit anytime by entering `0`  
- Locks access after too many failed attempts


## ⚙️ What’s Used

- **Input/Output:** `input()`, `print()`  
- **Looping:** `while` loop  
- **Comparison Operators:** `==`  
- **Counters:** to track attempts  
- **Conditional Statements:** `if`, `elif`, `else`  
- **Break Statement:** `break`


## 🚀 How to Run

1️⃣ Make sure you have Python installed.  
2️⃣ Save the script as `password_checker.py`.  
3️⃣ Open your terminal, navigate to the project folder, and run:  
```bash
python password_checker.py
```


## 💡 Example Output
```bash
Enter the Password(0 to exit): 1234
Access Denied, Try Again
2 attempts left.

Enter the Password(0 to exit): 0000
Access Denied, Try Again
1 attempts left.

Enter the Password(0 to exit): 1826
Access Granted
```
