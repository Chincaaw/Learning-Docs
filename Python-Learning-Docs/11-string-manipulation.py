# string manipulation

# concatenation
fisrtName = "Welt"
lastName = "Yang"
fullName = fisrtName + " " + lastName
print(fullName)

# calculate the length of the string
length = len(fullName)
print("length from '"+ fullName +"' = "+ str(length))

# operators for string

# check whether there are components in a string
letter = 'W'
check = letter in fullName
print(f'is there {letter} inside "{fullName}": {check}')

letter = 'w' # what if the letter is lower case
check = letter in fullName
print(f'is there {letter} inside "{fullName}": {check}') # result is false because in fullname string there is only a capital w

# check whether there are no components in a string
letter = 'W'
check = letter not in fullName 
print(f'is there {letter} inside "{fullName}": {check}')

# repeating strings
print('ha' * 5)

# indexing
## indexing is always start from 0.
print("index 0: ", fullName[0]) # return first latter of the string
print("index 3: ", fullName[3])
print("index -1: ", fullName[-1]) # indexing from behind
print("index [6, 8]: ", fullName[6:8]) # it means take the letters from index 6 to index before 8
print("index [0,2,4]: ", fullName[0:6:2]) # meaning take letters from index 0 to index before 6 in multiples of 2. [0, 2, 4]

# compare all the strings alphabetically based on the code points of initial characters.

# max
print('largest: ', max(fullName))
# min
print('smallest: ', min(fullName))

ascii_code = ord("z") # takes the ASCII number form of the letter z
print("ASCII code from z: ", str(ascii_code))
print(f"Character from ASCII code {ascii_code}: {chr(ascii_code)}")

# string methods
data = "Ular melingkar-lingkar di atas pagar"
total = data.count("a")
print(f"total a in '{data}': {total}")

## Changing Case

# Convert all characters to upper case

greeting = "Hai, My Name is Welt Yang!"
greeting = greeting.upper()
print("uppercase: ", greeting)

# Convert all characters to lower case

greeting = greeting.lower()
print("lowercase: ", greeting)

## is Method for Checking

greeting = "HELLO"
is_upper = greeting.isupper()
print(greeting + " is upper? " + str(is_upper))
greeting = greeting.lower()
is_upper = greeting.isupper()
print(greeting + " is upper? " + str(is_upper))

# islower() <- to check if all characters are lower case
# isalpha() <- to check if all characters are alphabets
# isalnum() <- alphabets and numbers?
# isdecimal() <- numeric?
# isspace() <- contains spaces, tabs, or newlines (\n)?
# istitle() <- first letter of each word capitalized

title = "Harry Potter and the Half-Blood Prince"
is_title = title.istitle()
print(title + " is title? " + str(is_title))

# startwith() and endwith() <-- neat

starts_with = "Welt Yang".startswith("Welt")
print(str(starts_with))
ends_with = "Welt Yang".endswith("Yang")
print(str(ends_with))

# join() and split() <-- for lazy people

words = ['I','love','you']
sentence = ' '.join(words)
print(words)
print(sentence)

sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()
print(sentence)
print(words)

sentence = "The-quick-brown-fox-jumps-over-the-lazy-dog"
words = sentence.split("-")
print(sentence)
print(words)

# Character Allocation
print("'left      '")

right_aligned = "right".rjust(20) # right align with 20 characters
print("'" + right_aligned + "'")

left_aligned = "left".ljust(20) # left align with 20 characters
print("'" + left_aligned + "'")

centered ="centered".center(20) # center align with 20 characters
print("'" + centered + "'")

centered ="centered".center(20,'-') # center align with 20 characters
print("'" + centered + "'")

# Opposite of Character Allocation
right_aligned = right_aligned.strip()
print("'" + right_aligned + "'")
centered = centered.strip('-')
print("'" + centered + "'")