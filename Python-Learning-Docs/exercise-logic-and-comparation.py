# less than, more than checking

x = float(input("Enter a number: "))

xLessThan = x < 10
xMoreThan = x > 0
yLessThan = x < 0
yMoreThan = x > 10

# 0 < x < 10
x_result = xLessThan and xMoreThan
# x < 0 or x >10
y_result = yLessThan or yMoreThan

print(f"0 < x < 10 : {x_result}, \n 0 > x > 10 : {y_result}")

# question number 1
# ---0+++5---8+++11---
x = float(input("question number 1, enter a number: "))

a = x > 0 and x < 5
b = x > 8 and x < 11
c = a or b
print("question 1 ",c)

# question number 
# +++0---5+++8---11+++
x = float(input("question number 1, enter a number: "))

a = 0 > x > 5
b = 8 > x > 11
c = a or b
print("question 1 ",c)
