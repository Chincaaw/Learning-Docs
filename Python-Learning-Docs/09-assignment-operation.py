# assignment operators

# operations that can be performed with abbreviation
# operations plus assignments

x = 5 # this is assignment

## arithmetic operation

# addition (+=)
x += 2 # x = x + 1
print("Result: ", x) # 5 + 2

# subtraction (-=)
x -= 2 # x = x - 1
print("Result: ", x) # 7 - 2

# multiplication (*=)
x *= 2 # x = x * 2
print("Result: ", x) # 5 * 2

# devision (/=)
x /= 2 # x = x / 2
print("Result: ", x) # 10 * 2

# floor division (//=)
x //= 2 # x = x // 2
print("Result: ", x) # 5 // 2

# modulus (%=)
x %= 2 # x = x % 2
print("Result: ", x) # 2 % 2

# exponentiation (**=)
x **= 2 # x = x ** 2
print("Result: ", x) # 0 ** 2

## bitwise operation

# OR (|=)
a = True
a |= False
print('value of a: ', a)
a = False
a |= True
print('value of a: ', a)

# AND (&=)
b = True
b &= False
print('value of b: ', b)
b = True
b &= True
print('value of b: ', b)

# XOR (^=)
c = True
c ^= False
print('value of c: ', c)
c = True
c ^= True
print('value of c: ', c)

# shifting
d = 0b0100
print('value of d: ', format(d, '04b'))
## shift left
d <<= 2
print('value of d <<= 2: ', format(d, '04b'))
## shift left
d >>= 1
print('value of d >>= 2: ', format(d, '04b'))



