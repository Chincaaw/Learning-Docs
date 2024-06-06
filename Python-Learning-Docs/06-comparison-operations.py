# comparison operators

# every result of b comparison operation is a boolean

## >, <, >=, <=, ==, !=

x = 4
y = 2

print(x, ' > ', y, ' : ', x > y)
print(x, ' < ', y, ' : ', x < y)
print(x, ' >= ', y, ' : ', x >= y)
print(x, ' <= ', y, ' : ', x <= y)
print(x, ' == ', y, ' : ', x == y)
print(x, ' != ', y, ' : ', x != y)

## 'is', 'is not'
# as an object identity comparison (not for literal form comparison)

a = 5 # This is an assignment to create an object
b = 5

# Python will store the same data in the same memory address
print('value a : ', a, ',id : ', hex(id(a)))
print('value b : ', b, ',id : ', hex(id(b)))
print('a is b : ', a is b)
print('a is not b : ', a is not b)