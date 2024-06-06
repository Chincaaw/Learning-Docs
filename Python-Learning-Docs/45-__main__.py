# __main__ is the top-level code environment.

# __name__ == "__main__" will occur 
# if it's in the main program file.

## __name__ in the main program file
print(f"Value of __name__ in main.py = '{__name__}'")

## __name__ in an external program file
import dummy_3

## Example usage of __main__

# Declaration
def add_function(x:int, y:int) -> int:
    return x + y

# Main function
if __name__ == "__main__":
    num1 = 5
    num2 = 10
    result = add_function(num1, num2)
    print(f"Addition result = {result}")

