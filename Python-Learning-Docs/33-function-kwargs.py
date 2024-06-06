# keyword Arguments
# **kwargs
def regular_function(name, height, weight):
    '''Regular function'''
    print(f"{name} has a height of {height} and weight of {weight}")

regular_function("Harry", 183, 79)

def kwargs_function(**kwargs):
    '''Keyword arguments function'''
    name = kwargs["name"]
    height = kwargs["height"]
    weight = kwargs["weight"]
    print(f"{name} has a height of {height} and weight of {weight}")

kwargs_function(name="Harry", height=183, weight=79)

# Case Study

def math_operation(*args, **kwargs):
    '''Perform mathematical operations'''
    output = 0
    if kwargs["operation"] == "add":
        for num in args:
            output += num
    elif kwargs["operation"] == "multiply":
        output = 1
        for num in args:
            output *= num
    else:
        print("No operation specified")

    return output

result = math_operation(1, 2, 3, 4, operation="add")
print(f"Sum result: {result}")

result = math_operation(1, 2, 3, 4, operation="multiply")
print(f"Multiplication result: {result}")
