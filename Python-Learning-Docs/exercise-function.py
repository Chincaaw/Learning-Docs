'''Function Practice'''

import os

def print_header():
    '''Function to print program header'''
    os.system("cls")
    print(f"{'AREA CALCULATION PROGRAM':^40}")
    print(f"{'AND RECTANGLE PERIMETER':^40}")
    print(f"{'-'*40:^40}")

def get_user_input():
    '''Function to get user input'''
    # Getting user input
    width = int(input("Enter the width value: "))
    length = int(input("Enter the length value: "))

    return width, length

def calculate_area(width, length):
    '''Function to calculate area'''
    return width * length

def calculate_perimeter(width, length):
    '''Function to calculate perimeter'''
    return 2 * (width + length)

def display_result(message, value):
    '''Function to display result'''
    print(f"Result of {message} calculation = {value}")

# Main program
while True:
    print_header()
    width, length = get_user_input()

    # Giving user options
    print("Choose an option:")
    print("1. Calculate area")
    print("2. Calculate perimeter")
    option = input("Enter your choice (1/2): ")

    if option == "1":
        area = calculate_area(width, length)
        display_result("area", area)
    elif option == "2":
        perimeter = calculate_perimeter(width, length)
        display_result("perimeter", perimeter)
    else:
        print("Invalid option!")

    is_continue = input("Continue (y/n)? ")
    if is_continue.lower() == "n":
        break

print("Program finished, thank you")
