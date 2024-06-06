# Format String

# Example of generic
# string
name = "welt"
format_str = f"hello {name}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# number
number = 2005.5
format_str = f"number = {number}"
print(format_str)

# integer
integer = 15
format_str = f"integer = {integer:d}"
print(format_str)

# number with thousands separator
number = 2000000
format_str = f"millions = {number:,}"
print(format_str)

# decimal number
number = 2005.54321
format_str = f"decimal = {number:.3f}"
print(format_str)

# leading zero
number = 2005.54321
format_str = f"decimal = {number:010.3f}" # 010 means sting will have 10 as string length, .3f mean sting can have 3 number after dot
print(format_str)

# display sign (+ or -)
negative_number = -10
positive_number = +10.1234
format_negative = f"negative = {negative_number:+d}"
format_positive = f"positive = {positive_number:+.2f}"

print(format_negative)
print(format_positive)

# format percentage
percentage = 0.045
format_percentage = f"percentage = {percentage:.2%}" # means string can have 2 numbers after dot

print(format_percentage)

# perform arithmetic operation inside placeholder
price = 10000
quantity = 5

format_string = f"total price = Rp. {price*quantity:,}"
print(format_string)

# formatting in other number systems (binary, octal, hexadecimal)

number = 255
format_binary = f"binary = {bin(number)}"
format_octal = f"octal = {oct(number)}"
format_hex = f"hexadecimal = {hex(number)}"

print(format_binary)
print(format_octal)
print(format_hex)
