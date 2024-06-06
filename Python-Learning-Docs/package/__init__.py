# first method (recommended)
# print("hallo world")

# example 1
from . import math

# example 2
from .math import multiplication

# example 3
from . import sub_package

# second method 
__all__ = [
    "math",
    "account"
]