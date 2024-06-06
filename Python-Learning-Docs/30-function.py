''' Function with arguments (inputs) '''

# Template
# def function_name(argument):
#     Function body

def greet_wizard(character_name):
    '''A function to greet wizards'''
    print(f"Welcome to the wizarding world, {character_name}!")

greet_wizard("Harry")
greet_wizard("Hermione")

def addition(num_1, num_2):
    '''A function for addition'''
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")

addition(3, 7)
addition(1000, 500)

def greet_muggles(muggle_list):
    '''A function to greet muggles'''
    for muggle in muggle_list:
        print(f"Dear {muggle}, greetings!")

muggle_friends = ["Ron", "Hermione", "Neville"]

greet_muggles(muggle_friends)

'''Functions with Return Values'''

# Function template with return
# def function_name(argument):
#     function body
#     return output

# Square function
def square(input_number):
    '''Square function'''
    squared_output = input_number**2
    return squared_output

harry_potter_age = square(11)
print(harry_potter_age)

print(square(13))

total = 20 + square(9)
print(total)

# Addition function
def addition(num_1, num_2):
    '''Function with multiple inputs and return'''
    return num_1 + num_2

hermione_granger_score = addition(15, 17)
print(hermione_granger_score)

# Math operations function
def math_operations(num_1, num_2):
    '''Function with multiple return values'''
    addition_result = num_1 + num_2
    subtraction_result = num_1 - num_2
    multiplication_result = num_1 * num_2
    division_result = num_1 / num_2

    return addition_result, subtraction_result, multiplication_result, division_result

ron_weasley, draco_malfoy, neville_longbottom, hagrid = math_operations(12, 7)

print(f"Addition result = {ron_weasley}")
print(f"Subtraction result = {draco_malfoy}")
print(f"Multiplication result = {neville_longbottom}")
print(f"Division result = {hagrid}")

'''Default Argument'''

# Example 1
def greet_person(name = "Handsome"):
    '''Function with default argument'''
    print(f"Hello {name}")

greet_person("Harry")
greet_person()

# Example 2
def greet_someone(name, message = "How are you?"):
    '''Function with one regular input and one default argument'''
    print(f"Hey {name}, {message}")

greet_someone("Ron", "Hi Handsome")
greet_someone("Hermione")

# Example 3
def calculate_power(number, power=2):
    '''Function to calculate power'''
    result = number**power
    return result

print(calculate_power(2, 4))

result = calculate_power(power=3, number=5)
print(result)

# Example 4
def calculate_sum(input1=1, input2=2, input3=3, input4=4):
    '''Function to calculate sum with default values'''
    result = input1 + input2 + input3 + input4
    return result

print(calculate_sum())
print(calculate_sum(input3=10))
