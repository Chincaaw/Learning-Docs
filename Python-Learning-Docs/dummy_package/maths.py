'''Math module'''

# Function to add numbers
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# Function to multiply numbers
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Function to calculate power of a number
def power(n):
    return lambda x: x**n

# Testing
# add_result = add(2, 3, 4) # Example usage of add function
# print(add_result)
# multiply_result = multiply(2, 3, 4) # Example usage of multiply function
# print(multiply_result)
# power_result = power(3) # Example usage of power function
# print(power_result(2))
