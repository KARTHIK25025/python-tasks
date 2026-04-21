# main.py

import calculator

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", calculator.add(a, b))

elif choice == 2:
    print("Result:", calculator.subtract(a, b))

elif choice == 3:
    print("Result:", calculator.multiply(a, b))

elif choice == 4:
    print("Result:", calculator.divide(a, b))

else:
    print("Invalid choice")