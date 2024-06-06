# loop control statements

# Example of using pass:
# Pass is used when you need to write a statement that does nothing.
# It's useful when you're in the development process and want to leave a part of the code unimplemented.
for i in range(5):
    if i == 2:
        pass  # Do nothing when i is equal to 2
    else:
        print(i)

# Example of using break:
# Break is used to abruptly stop a loop when a certain condition is met.
# Here, the loop will stop when i equals 2.
for i in range(5):
    if i == 2:
        break  # Stop the loop when i equals 2
    else:
        print(i)

# Example of using continue:
# Continue is used to skip the rest of the code inside the loop and continue to the next iteration.
# Here, when i equals 2, the statement print(i) will not be executed, and the iteration will proceed to the next value of i.
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the code inside the loop when i equals 2
    else:
        print(i)
