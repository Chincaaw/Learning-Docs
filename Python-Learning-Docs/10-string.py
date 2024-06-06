# string

data = "this is a string that store inside a variable"
print(data)
print(type(data))

## 1. how to make a string

'''
    1. by using single quote ('..')
    2. by using double quote ("..")
'''

data = 'single quote'
print(data)

data = "double quote"
print(data)

# other version of string
print('"Hello there, how are you?"')
print("'Herlo there, how are you?'")
print("i'm fine thanks")

## 2. string with backslash (\)
print('i\'m fine thanks')
print('g\'day, isn\'t it?')

# how to add backslash to string
print("C:\\user\\achllx")

# how to tab in string
print('\t hallo world')

# how to do backspace
print("hello \b world")

# how to make new line
print("first line.\nsecond line.") # LF -> line feed -> unix, macos, linux
print("first line.\rsecond line.") # CR -> carriage return -> commodore, acorn, lisp 
print("first line.\r\nsecond line.") # CRLF -> line feed carriage return -> used by windows

## 3. raw string
# beware
print('C:\new folder') # this will trigger \n that create new line
print(r'C:\new folder') # use this instead

# multiple literal string
print("""
Name: achllx
age: 22
""")

# combining raw string with multiple literal string
print(r"""
Name: achllx
age: 22
folder: C:\new folder
""")
