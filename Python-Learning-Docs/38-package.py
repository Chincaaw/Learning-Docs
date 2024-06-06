import dummy_package.maths
from dummy_package import maths
from dummy_package.maths import power as x

sum_result = dummy_package.maths.add(1, 2, 3, 4, 5)
print(f"The sum result from the package is = {sum_result}")

sum_result = maths.multiply(90, 10)
print(f"The multiply is = {sum_result}")

sum_result = x(2)
print(f"The power is = {sum_result(3)}")
