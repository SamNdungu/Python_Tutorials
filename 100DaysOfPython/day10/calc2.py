# Calculator project
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divind
def divide(n1, n2):
    return n1 / n2

# Creating a dictionary to store symbols as keys and functions as values
operations = {
    "+":  add,
    "-":  subtract,
    "*":  multiply,
    "/":  divide,
}

def calculator():

    print(logo)

    num1 = float(input("What is your first number?: "))

    # for loop to loop through keys
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is your next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 == answer
        else:
            should_continue = False
            calculator()
calculator()           
