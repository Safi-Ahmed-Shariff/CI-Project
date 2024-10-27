# main.py

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract_numbers(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply_numbers(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def divide_numbers(num1, num2):
    """Returns the division of two numbers. Raises an error if divided by zero."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

if __name__ == "__main__":
    # Example usage
    print("Addition:", add_numbers(5, 3))
    print("Subtraction:", subtract_numbers(5, 3))
    print("Multiplication:", multiply_numbers(5, 3))
    print("Division:", divide_numbers(5, 3))
