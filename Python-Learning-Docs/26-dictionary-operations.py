# Dictionary operators

# Dictionary containing character names and descriptions
character_dict = {
    "harry": "Harry Potter, the chosen one",
    "hermione": "Hermione Granger, the brightest witch of her age",
    "ron": "Ron Weasley, the loyal friend"
}

# Length of the dictionary
DICT_LENGTH = len(character_dict)
print(f"Dictionary length: {DICT_LENGTH}")

# Checking if a key exists
KEY_TO_CHECK = "harry"
KEY_EXISTENCE = KEY_TO_CHECK in character_dict
print(f"Is {KEY_TO_CHECK} in character_dict? {KEY_EXISTENCE}")

# Accessing values using keys
print(character_dict["harry"])
print(character_dict.get("hermione"))
print(character_dict.get("dobby", "Key not found")) # Check key with custom message if not found  

# Updating data
character_dict["harry"] = "Harry Potter, the boy who lived"
print(character_dict)
character_dict["neville"] = "Neville Longbottom, the brave Gryffindor"
print(character_dict)

character_dict.update({"harry": "Harry Potter, the chosen one"})
print(character_dict)
character_dict.update({"luna": "Luna Lovegood, the dreamy witch"})  # Add if not present
print(character_dict)

# Deleting data from the dictionary
del character_dict["neville"]
