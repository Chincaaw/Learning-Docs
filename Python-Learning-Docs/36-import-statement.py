# import

# Its function is to retrieve
# programs from external .py files

# 1. To connect to external programs
import dummy_1 as data
import dummy_2 as func

# Data is in the namespace of data_storage
print(data.name)

# 2. Import with functions
result = func.division(4, 2)
print(result)