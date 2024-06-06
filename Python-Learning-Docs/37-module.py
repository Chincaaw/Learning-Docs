# import dummy_2 
import dummy_2 as math # give alias
# from dummy_2 import addition, multiplication, power
from dummy_2 import addition as add, multiplication as multi, power # give alias for each external function.\

result = add(8,5)
print(result)

result = math.multiplication(2, 5)
print(result)\

result = power(2)
print(result(3))