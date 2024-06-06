# *args usage

# Function to display name, height, and weight
def display_info(name, height, weight):
    print(f"{name} has a height of {height} and weighs {weight}")

# Using individual arguments
display_info("Harry", 170, 60)

# Using a list as input
def display_info(data_list):
    name = data_list[0]
    height = data_list[1]
    weight = data_list[2]
    print(f"{name} has a height of {height} and weighs {weight}")

display_info(["Ron", 180, 70])

# Introduction to *args

def display_info(*args):
    name = args[0]
    height = args[1]
    weight = args[2]
    print(f"{name} has a height of {height} and weighs {weight}")

display_info("Hermione", 160, 50)

# Case study

def sum_values(*data):
    # Data type of 'data' is tuple, which is iterable
    total = 0
    for num in data:
        total += num
    return total

result = sum_values(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"result = {result}")

result = sum_values(10, 5, 15)
print(f"result = {result}")
