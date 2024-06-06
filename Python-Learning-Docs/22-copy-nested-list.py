# Original data
original_data_0 = [1, 2]
original_data_1 = [3, 4]

# 2D data list containing original data and a scalar value
data_2D = [original_data_0, original_data_1, 10]

# Create a shallow copy of the 2D data list
shallow_copy_2D = data_2D.copy()

print(f"Original data = {data_2D}")
print(f"Shallow copy of data = {shallow_copy_2D}")

# Accessing data from nested lists
nested_data = data_2D[1][0]
print(f"Nested data = {nested_data}")

# Display memory addresses
print(f"Original data address = {hex(id(data_2D))}")
print(f"Shallow copy address = {hex(id(shallow_copy_2D))}")

print("Memory addresses of the first member")
print(f"Original data address = {hex(id(data_2D[0]))}")
print(f"Shallow copy address = {hex(id(shallow_copy_2D[0]))}")

# Modifying data in the original and shallow copy
data_2D[1][0] = 5
data_2D[2] = 9

print(f"Modified data = {data_2D}")
print(f"Shallow copy after modification = {shallow_copy_2D}")

# Using deepcopy
from copy import deepcopy

# Create a deep copy of the original 2D data list
deep_copy_2D = deepcopy(data_2D)

print(f"Original data address = {hex(id(data_2D))}")
print(f"Deep copy address = {hex(id(deep_copy_2D))}")

print("Memory addresses of the first member")
print(f"Original data address = {hex(id(data_2D[0]))}")
print(f"Deep copy address = {hex(id(deep_copy_2D[0]))}")

# Modify data in the original and observe the copies
data_2D[1][0] = 30
print(f"Original data = {data_2D}")
print(f"Shallow copy = {shallow_copy_2D}")
print(f"Deep copy = {deep_copy_2D}")
