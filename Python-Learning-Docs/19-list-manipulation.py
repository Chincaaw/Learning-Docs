# list manipulation

# index   0(-3)  1(-2)  2(-1)
names = ["John","Doe","Smith"]

# Accessing data from this list
first_data = names[0]
print(f"First data (index 0) = {first_data}")

last_data = names[-1]
print(f"Last data = {last_data}")

other_data = names[-3]
print(f"Data at index -3 = {other_data}")

# Retrieving information about the length of the list
data_length = len(names)
print(f"Data length = {data_length}")

## Manipulating list data

# Adding items to the list at specific positions
print(f"Data before insertion = \n{names}")

names.insert(1, "Michael")
print(f"Data after insertion = \n{names}")

# Adding at the end of the list
names.append("Emily")
print(f"Data after another addition =\n{names}")

# Adding a list with another list
new_names = ["Alice", "Bob", "Charlie"]
names.extend(new_names)
print(f"Combined data =\n{names}")

# Modifying data
# Let's change "Doe" to "David"
names[2] = "David"
print(f"Modified data = \n{names}")

# Removing data

names.remove("Alice")
print(f"Data after removal = \n{names}")

# Removing the last data
last_data_removed = names.pop()
print(f"Last data removed = \n{names}")

print(last_data_removed)


# List of numbers
number_data = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]

print(f"Number data = \n{number_data}")

# Counting data
count_4 = number_data.count(4)
count_3 = number_data.count(3)

print(f"Count of 4 = {count_4}")
print(f"Count of 3 = {count_3}")

# Retrieving data positions (indexes)
names = ["John", "Alice", "Bob", "Eve"]

print(f"Names = {names}")

index_bob = names.index("Bob")
index_eve = names.index("Eve")
print(f"Index of Bob = {index_bob}")
print(f"Index of Eve = {index_eve}")

# Sorting lists
print(f"Number data before sorting = \n{number_data}")
number_data.sort()
print(f"Sorted number data = \n{number_data}")

print(f"Names = {names}")
names.sort()
print(f"Sorted names = {names}")

# Reversing the list
number_data.reverse()
names.reverse()
print(f"Reversed data = \n{number_data} \n{names}")
