import datetime
from collections import Counter

# Get current date and time
current_time = datetime.datetime.now()
print(f"Current datetime: {current_time}")
print(f"Year: {current_time.year}")
print(f"Day: {current_time.strftime('%A')}")

# Sample data with character names from Harry Potter
characters = ["harry", "hermione", "ron", "dobby", "harry", "dobby", "harry"]

# Count occurrences of each character
character_count = Counter(characters)

print(f"Character counts: {character_count}")
print(f"Occurrences of Harry: {character_count['harry']}")
print(f"Occurrences of Dobby: {character_count['dobby']}")

import io

# Open and read a text file
text_file = io.open("text_file.txt", "r")
print(text_file.read())
