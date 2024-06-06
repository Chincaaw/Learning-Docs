# List Duplication Techniques

# Original list
original_list = ["Ucup", "Otong", "Dudung"]
print(f"original_list = {original_list}")

# Using assignment to create a reference
reference_list = original_list  # pass by reference
print(f"reference_list = {reference_list}")

# Modifying a member of 'original_list' affects both lists
original_list[1] = "Michael"
reference_list.sort()
print(f"original_list = {original_list}")
print(f"reference_list = {reference_list}")

# Address of both 'original_list' and 'reference_list'
print(f"address original_list = {hex(id(original_list))}")
print(f"address reference_list = {hex(id(reference_list))}")

# Duplication using copy method
print("Creating 'copied_list' using original_list.copy()")
copied_list = original_list.copy()  # full duplication / new data
print(f"address original_list = {hex(id(original_list))}")
print(f"address reference_list = {hex(id(reference_list))}")
print(f"address copied_list = {hex(id(copied_list))}")

print(f"original_list = {original_list}")
print(f"reference_list = {reference_list}")
print(f"copied_list = {copied_list}")

# Modifying an element in 'copied_list' does not affect the others
print("Modifying data at index 0 in 'copied_list'")
copied_list[0] = "Dadang"
print(f"original_list = {original_list}")
print(f"reference_list = {reference_list}")
print(f"copied_list = {copied_list}")

# Modifying an element in 'original_list' does not affect 'copied_list'
print("Modifying data at index 1 in 'original_list'")
original_list[1] = "Otong"
print(f"original_list = {original_list}")
print(f"reference_list = {reference_list}")
print(f"copied_list = {copied_list}")
