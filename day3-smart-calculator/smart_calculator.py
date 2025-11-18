import re  # Regular expressions

# -----------------------------
# Functions
# -----------------------------
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def modulus(x, y):
    return x % y

# -----------------------------
# Main program
# -----------------------------
try:
    # Ask user for input
    cal = input("Enter an equation (e.g., -12 + 34): ")

    # Regex pattern to capture optional minus, numbers, operator, optional spaces
    match = re.fullmatch(r"\s*(-?\d+)\s*([+\-*/%])\s*(-?\d+)\s*", cal)
    if not match:
        raise ValueError("Invalid format. Use: number operator number (e.g., -12 + 34)")

    num1 = int(match.group(1))
    op = match.group(2)
    num2 = int(match.group(3))

    # Perform calculation using match-case
    match op:
        case '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        case '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        case '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        case '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        case '%':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        case _:
            raise ValueError(f"Unsupported operator: {op}")

except ValueError as ve:
    print("Error:", ve)
