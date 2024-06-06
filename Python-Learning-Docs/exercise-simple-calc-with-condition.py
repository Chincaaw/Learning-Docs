# Input numbers a, b, and the operator
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform arithmetic operation based on the operator
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    # Avoid division by zero
    if b != 0:
        result = a / b
    else:
        print("Error: Cannot divide by zero!")
        result = None
else:
    print("Error: Invalid operator!")
    result = None

# Output the result of the arithmetic operation
if result is not None:
    print(f"Result of {a} {operator} {b} = {result}")
