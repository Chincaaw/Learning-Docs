# Looping through lists

# Using for loop
print("For Loop")
number_collection = [4, 3, 2, 5, 6, 1]

for number in number_collection:
    print(f"number = {number}")

participants = ["Kiana", "Bronya", "Himeko", "Raiden", "Mei"]

for name in participants:
    print(f"name = {name}")

# Using for loop with range
print("\nFor Loop and range")
number_collection = [10, 5, 4, 2, 6, 5]

length = len(number_collection)

for i in range(length):
    print(f"number = {number_collection[i]}")

# Using while loop
print("\nWhile loop")
number_collection = [10, 5, 4, 2, 6, 5]

length = len(number_collection)
i = 0

while i < length:
    print(f"number = {number_collection[i]}")
    i += 1

# List comprehension
print("\nList Comprehension")
data = ["Kiana", 1, 2, 3, "Bronya"]

[print(f"data={item}") for item in data]

numbers = [10, 5, 4, 2, 6, 5]

squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# Using enumerate
print("\nEnumerate")
data_list = ["Kiana", 1, 2, 3, "Bronya"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")
