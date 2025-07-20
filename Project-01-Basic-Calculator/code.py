# Simple Calculator

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

choice = int(input("\nEnter your choice (1/2/3/4): "))

if choice == 1:
    print("Sum:", n1 + n2)
elif choice == 2:
    print("Difference:", n1 - n2)
elif choice == 3:
    print("Product:", n1 * n2)
elif choice == 4:
    if n2 != 0:
        print("Quotient:", n1 / n2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
