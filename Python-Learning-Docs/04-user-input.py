# user input

# Whatever user input, the data entered will be string type
data = input("Enter data: ")

print("data = ", data)
print("type = ", type(data))

# changin user input data types

## number
number = float(input("Enter integer: "))

print("data = ", number)
print("type = ", type(number))

## boolean
biner = bool(int(input("Enter integer: ")))

print("data = ", biner)
print("type = ", type(biner))