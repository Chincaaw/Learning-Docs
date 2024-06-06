# Dictionary of friends' names and their nicknames
friends = {
    "harry": "harry potter",
    "ron": "ron weasley",
    "hermione": "hermione granger",
    "neville": "neville longbottom",
    "ginny": "ginny weasley"
}

# Looping through keys directly
for friend in friends:
    print(friend)

# Using keys() method to get keys
keys = friends.keys()
print(keys)

# Looping through keys and accessing values using get()
for key in friends.keys():
    print(friends.get(key))

# Using values() method to get values
values = friends.values()
print(values)

# Looping through values directly
for value in friends.values():
    print(value)

# Using items() method to get key-value pairs
items = friends.items()
print(items)

# Looping through items and unpacking key-value pairs
for key, value in friends.items():
    print(f"key = {key}, value = {value}")
