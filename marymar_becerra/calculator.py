def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Get a valid operation from the user."""
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        print("Invalid operation. Please choose +, -, *, or /.")

def calculate(num1, num2, operation):
    """Perform the calculation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 / num2

def main():
    """Main calculator function."""
    print("Welcome to the Calculator!")
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    
    if result is not None:
        # Format the result nicely
        if result == int(result):
            result = int(result)
        print(f"Result: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()