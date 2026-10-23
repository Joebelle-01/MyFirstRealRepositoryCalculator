"""
Simple CLI Calculator
Author: Joebelle Dumapias
Section: IT3R10
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is undefined."
    return a % b

def main():
    print("=== Simple Calculator ===")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    
    choice = input("Enter choice (1-6): ").strip()
    
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please select a number between 1 and 6.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        print(f"Result: {num1} % {num2} = {modulo(num1, num2)}")

if __name__ == "__main__":
    main()