# 1. Write mode: Overwriting

# It creates a new file if it doesn't exist,
# then overwrites its contents.

with open("text_file_1.txt", 'w', encoding="utf-8") as file:
    file.write("harry the wizard")

# 2. Append mode: Adding content

# It creates a new file if it doesn't exist,
# then appends content to it.

with open("text_file_2.txt", 'w', encoding="utf-8") as file:
    file.write("ron the wizard\n")

with open("text_file_2.txt", 'a', encoding="utf-8") as file:
    file.write("hermione the wizard\n")

# 3. Read & Write mode: Combination

# It creates a new file if it doesn't exist,
# then allows reading and writing content.

with open("text_file_3.txt", 'w', encoding="utf-8") as file:
    file.write("file number three\n")

with open("text_file_3.txt", 'r+', encoding="utf-8") as file:
    file.write("line-1 \n")
    file.write("line-2 \n")
    file.write("line-3 \n")

with open("text_file_3.txt", 'r+', encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("text_file_3.txt", 'r+', encoding="utf-8") as file:
    file.write("dobby")  # Overwrites content according to the length of data
