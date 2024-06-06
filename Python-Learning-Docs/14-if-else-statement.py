# if else statement

# Input
number = int(input("Enter a number: "))  # Prompt user to enter a number and convert it to an integer

# Check if the number is positive, negative, or zero
if number > 0:  # Check if the number is greater than 0
    print("The number is positive.")  # Print message if the number is positive
elif number < 0:  # If the number is not greater than 0, check if it's less than 0
    print("The number is negative.")  # Print message if the number is negative
elif number == 0:  # If the number is neither greater than nor less than 0, check if it's equal to 0
    print("The number is zero.")  # Print message if the number is zero
else:  # If none of the above conditions are met
    print("Invalid input.")  # Print message for invalid input
