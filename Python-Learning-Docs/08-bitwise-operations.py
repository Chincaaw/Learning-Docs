# bitwise operators
#-> operation of each bit

# int 2 -> 0 0 0 0 0 0 1 0

# how to get the number that corresponds to an integer value by calculating the exponents of the bits
# Put 1 in the bit index and multiply the index by 2

# example

# int 2 -> 0 0 0 0 0 0 1 0
#    index 7 6 5 4 3 2 1 0
# 2**1 = 2, so bit for integer 2 is 00000010
print('Binary form of 2: ',format(2, '08b'))

# int 9 -> 0 0 0 0 1 0 0 1
#    index 7 6 5 4 3 2 1 0
# 2**3 = 2 + 2**0 = 1, so bit for integer 9 is 00001001
print('Binary form of 9: ',format(9, '08b'))

# bitwise operator
# 2 | 1 (2 or 1)
# 2 -> 0 0 0 0 0 0 1 0
# 1 -> 0 0 0 0 0 0 0 1
#     ----------------- (0or0=0, 1or0=1, 1or1=1)
#      0 0 0 0 0 0 1 1

# 2**0 + 2**1 = 3
# the result from 2 | 1 is 3

a = 9
b = 5

# OR (|)
c = a | b # OR
print("========OR========")
print(f' {a} | {b} : ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print(f'Binary form of {b}: ',format(b, '08b'))
print('------------------------------ (|)')
print('result: ',format(c, '08b'))

# AND (&)
c = a & b # AND
print("========and========")
print(f' {a} & {b} : ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print(f'Binary form of {b}: ',format(b, '08b'))
print('------------------------------ (&)')
print('result: ',format(c, '08b'))

# XOR (^)
c = a ^ b # XOR

print("========XOR========")
print(f' {a} ^ {b} : ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print(f'Binary form of {b}: ',format(b, '08b'))
print('------------------------------ (^)')
print('result: ',format(c, '08b'))

# NOT (~)
c = ~ a # NOT

print("========XOR========")
print(f'~ {a}: ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print('------------------------------ (~)')
print('result: ',format(c, '08b'))

## shifting

#shif right (>>)
c = a >> 2

print("========>>========")
print(f'{a} >> 2 : ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print('------------------------------ (>>)')
print('Result: ',format(c, '08b'))

#shif left (<<)
c = a << 2

print("========<<========")
print(f'{a} >> 2 : ', c)
print(f'Binary form of {a}: ',format(a, '08b'))
print('------------------------------ (<<)')
print('Result: ',format(c, '08b'))