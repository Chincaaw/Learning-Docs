def division(a: float, b: float) -> float:
    return a/b

def addition(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def multiplication(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def power(n:int):
    # Returns a lambda function that raises a number to the power of n
    return lambda number: number**n
