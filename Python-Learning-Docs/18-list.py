# list

# Collection of numbers
number_data = [3, 8, 4, 6]
print(number_data)

# Collection of strings
string_data = ["apple", "banana", "orange"]
print(string_data)

# Collection of booleans
boolean_data = [True, False, True]
print(boolean_data)

# Mixed collection
mixed_data = [2, "pizza", 5, "burger", True, "apple", False]
print(mixed_data)

## Alternative ways to create lists

# Using range function
data_range = range(0, 15, 3)  # range(start, stop, step)
print(data_range)
range_list = list(data_range)
print(range_list)

# Using for loop and list comprehension
squared_list = [num ** 2 for num in range(0, 10)]
print(squared_list)

# Using for loop with if statement
filtered_list = [num for num in range(0, 10) if num != 7]
print(filtered_list)

# Using for loop with if statement (filtering even numbers)
even_numbers = [num for num in range(0, 10) if num % 2 == 0]
print(even_numbers)

# Using for loop with if statement (filtering odd numbers and squaring them)
odd_squared = [num ** 2 for num in range(0, 10) if num % 2 != 0]
print(odd_squared)
