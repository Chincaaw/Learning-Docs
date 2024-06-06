import numpy as np

# List of integers
harry_potter_characters = [1, 2, 3, 4]

# Converting list to numpy array
harry_potter_vector = np.array([1, 2, 3, 4])

print(f"harry_potter_characters = {harry_potter_characters}")

# Performing element-wise square operation on the array
print(f"harry_potter_vector = {harry_potter_vector}")
print(f"Square of harry_potter_vector = {harry_potter_vector**2}")

# Performing scalar multiplication on the array
print(f"Multiplying harry_potter_vector by 5 = {harry_potter_vector*5}")

# Creating a 2x2 matrix
harry_potter_matrix = np.array([(1, 2), (3, 4)])
print(f"harry_potter_matrix = \n{harry_potter_matrix}")

# Performing element-wise square operation on the matrix
print(f"Square of harry_potter_matrix = \n{harry_potter_matrix**2}")

# Creating a 2x2 matrix of zeros
zeros_matrix = np.zeros((2, 2))
print(f"Zeros matrix = \n{zeros_matrix}")

# Creating a 2x2 matrix of ones
ones_matrix = np.ones((2, 2))
print(f"Ones matrix = \n{ones_matrix}")

# Performing element-wise addition, squares, and addition again
total = harry_potter_matrix + harry_potter_matrix**2 + ones_matrix
print(f"Total = \n{total}")
