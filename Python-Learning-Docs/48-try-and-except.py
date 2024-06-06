# Exceptions occur when a program encounters errors during runtime.

## Simple example to handle an exception

# Using a simple example
# user_input = int(input("Enter a number: "))  # Commented out to avoid interrupting the flow
# result = nan  # Commented out to avoid uninitialized variable error

# try:
#     result = 10 / user_input
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# print(f"Result = {result}")

# Example in an application

while True:
    divisor = int(input("Enter the divisor: "))
    try:
        result = 10 / divisor
        print(f"Result = {result}")
        continue_prompt = input("Continue (y/n)? ")
        if continue_prompt == "n":
            break
    except ZeroDivisionError:
        print("Cannot divide by zero, please enter a different input")

print("End of program 1")

# Example application to create a data.txt file
try:
    with open("data.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("data.txt file not found, creating a new file")
    with open("data.txt", 'w', encoding='utf-8') as file:
        file.write("new file")

print("End of program 2")

# # Example of handling exceptions

# from numbers import Number

# def add_numbers(x, y):
#     # Check if both inputs are numbers
#     if not isinstance(x, Number) or not isinstance(y, Number):
#         raise ValueError("Inputs must be numbers")
#     return x + y

# print(add_numbers(5, 6))

# # Using try-except block to handle specific exception
# divider = 0
# try:
#     result = 10 / divider
# except ZeroDivisionError as error_msg:
#     print(error_msg)
