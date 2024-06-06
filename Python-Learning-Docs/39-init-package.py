# first method (recommended)
import package
from package import multiplication
# import package inside a package
# import package.sub_package.greeting

# example 1
result = package.math.addition(2, 2)
print(result)

# example 2
result = package.multiplication(2, 2)
print(result)
result = multiplication(2, 2)
print(result)

# example 3
package.sub_package.greeting.greet('Harry Potter')
package.sub_package.greet("Heromine")


# # second method
# from package import *

# result = math.addition(2, 2)
# print(result)
