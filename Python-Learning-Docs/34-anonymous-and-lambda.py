# Lambda function

# Regular function for squaring a number
def square_number(num):
    return num**2

print(f"Result of square function = {square_number(3)}")

# Trying with lambda
square = lambda num: num**2
print(f"Result of lambda square = {square(5)}")

power = lambda num, pow: num**pow
print(f"Result of lambda power = {power(4,2)}")

## What's the use?

# Sorting a regular list
characters = ["Harry", "Hermione", "Ron"]
characters.sort()
print(f"Sorted list = {characters}")

# Sorting by length using a regular function
def name_length(name):
    return len(name)

characters.sort(key=name_length)
print(f"Sorted list by length = {characters}")

# Sorting using lambda
characters = ["Harry", "Hermione", "Ron"]
characters.sort(key=lambda name: len(name))
print(f"Sorted list by lambda = {characters}")

# Filtering
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Filtering numbers less than 5
new_numbers = list(filter(lambda x: x < 5, numbers))
print(new_numbers)

# Filtering even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Filtering odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Filtering multiples of 3
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_3)

# Anonymous function
# Currying

# Regular function for power
def power(num, n):
    result = num**n
    return result

data_result = power(5, 2)
print(f"Regular function = {data_result}")

# Currying implementation
def power(n):
    return lambda num: num**n

power_2 = power(2)
print(f"Power 2 = {power_2(5)}")
power_3 = power(3)
print(f"Power 3 = {power_3(3)}")
print(f"Arbitrary power = {power(4)(5)}")
