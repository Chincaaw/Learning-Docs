# datatypes

# x = 10, x is a variable with value 10

## normal data types

# integer
data_integer = 10
print("Data : ", data_integer)
print("Type : ", type(data_integer))

# float
data_float = 1.5
print("Data : ", data_float)
print("Type : ", type(data_float))

# string
data_string = "Hello World"
print("Data : ", data_string)
print("Type : ", type(data_string))

# boolean
data_boolean = True
print("Data : ", data_boolean)
print("Type : ", type(data_boolean))

## special data types

# complex
data_complex = complex(5,6)
print("Data : ", data_complex)
print("Type : ", type(data_complex))

# c language data types
from ctypes import c_double, c_char # we can use all c langugae data types

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print("Type : ", type(data_c_double))