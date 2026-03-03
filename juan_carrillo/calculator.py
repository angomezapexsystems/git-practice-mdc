#!/usr/bin/env python3

"""Simple calculator performing arithmetic operations on two numbers.
"""

def multiply(a, b):
    return a * b


def main():
    """Entry point when run as a script."""
    print("Basic calculator - enter two numbers and performs a multiplication.")
    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
    except ValueError:
        print("Invalid input; please enter numeric values.")
        return

    try:
        
    result = multiply(x, y)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
