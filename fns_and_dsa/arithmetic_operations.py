# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
