''' Function with Type Hints '''

# Standard function structure

'''
Case study
def function(parameter):
    result = parameter**2
    print(result)

function(1)
function("Harry")
function(True)
'''

# Usage of type hints

import string

def ten_power(argument:int) -> int:
    '''Function with hints'''
    output = 10**argument
    return output

RESULT = ten_power(4)
print(RESULT)

def display(character_name:string):
    '''Function to display character name'''
    print(character_name)

display("Hermione")
