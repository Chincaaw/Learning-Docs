# Copying a dictionary

# Original dictionary with character names from Harry Potter
harry_potter_friends = {
	"harry": "harry the wizard",
	"ron": "ron the red-haired",
	"hermione": "hermione the clever",
	"ginny": "ginny the brave",
	"neville": "neville the courageous"
}

# Creating a copy of the original dictionary
wizard_friends = harry_potter_friends.copy()

# Modifying the original dictionary
harry_potter_friends["harry"] = "harry the chosen one"

# Printing both dictionaries after modification
print(f"harry_potter_friends: {harry_potter_friends}\n")
print(f"wizard_friends: {wizard_friends}\n")

# Removing an item from the copied dictionary
removed_data = wizard_friends.pop("ginny")
print(f"data removed: {removed_data}\n")
print(f"wizard_friends: {wizard_friends}\n")

# Removing the last item from the copied dictionary
last_data = wizard_friends.popitem()
print(f"last data: {last_data}\n")
print(f"wizard_friends: {wizard_friends}\n")
