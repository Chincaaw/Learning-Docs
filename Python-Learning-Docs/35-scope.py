## Global and Local Scope

# Global variable
global_name = "harry"  # <- this is a global variable

# Accessing global variable within a function
def function1():
    print(f"Function displays {global_name}")

function1()

# Accessing global variable within a loop
for i in range(0, 5):
    print(f"Loop {i} - {global_name}")

# Conditional statement
if True:
    print(f"If statement displays {global_name}")


## Local Scope Variables

def function2():
    local_name = "hermione"  # <- local scope variable

function2()
# print(local_name) # cannot be done

## Example 1: Variable access
def say_harry():
    print(f"Hello {name}")

name = "Harry"
say_harry()

## Example 2: Modifying global variables
number = 0
character = "Ron"

def modify(new_value, new_name):
    global number  # this function has access to modify number
    global character
    number = new_value
    character = new_name

print(f"Before {number, character}")
modify(10, "Harry")
print(f"After {number, character}")

## Example 3:
number = 0

for i in range(0, 5):
    number += i
    dummy_number = 0

print(number)

if True:
    number = 5
    dummy_number = 10

print(number)
print(dummy_number)
