## Reading External File Tutorial

print(3 * "=", " Reading txt file ", 3 * "=")
# Open the external file for reading
file = open("text_file.txt", mode="r")
# file = open("text_file", mode="w")

# Check if the file is readable and writable
print(f"Readable status: {file.readable()}")
print(f"Writable status: {file.writable()}")

# Read the entire file content
# print(file.read())

# Read in line
print(file.readline()) # Read the first line
print(file.readline()) # Read the second line 
# and so on

# Read the entire file content as list
print(file.readlines())

# Check if the file is closed
print(f"Is the file closed: {file.closed}")
file.close()  # Close the file
print(f"Is the file closed: {file.closed}")


## Technique to open file using 'with'

print("\n", 3 * "=", " Reading txt file with 'with' ", 3 * "=")

# this technique is to auto close the file
with open("text_file.txt", mode="r") as file:
    # Read the first line of the file
    content = file.readline()
    print(content, end="")
    print(f"Is the file closed: {file.closed}")

print(f"Is the file closed: {file.closed}")
