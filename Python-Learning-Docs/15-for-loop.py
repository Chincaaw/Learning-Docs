# for loop

# Using list
number_list = [0, 2, 4, 8, 10]
print(number_list)

for num in number_list:
    print(f"Current num -> {num}")

print("End of program 1 \n")

# Using range
x = range(5) # can be store the range of number first 
# example, for num in x:
for num in range(5): # or can be use it straight away
    print(f"Current num -> {num}")

print("End of program 2 \n")

for num in range(1, 10):
    print(f"Current num -> {num}")

print("End of program 3 \n")

# Using string
data_str = "Hallo World"

for letter in data_str:
    print(letter)

print("End of program 4 \n")
