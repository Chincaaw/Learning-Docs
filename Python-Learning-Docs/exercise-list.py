# Game Character List Program

character_list = []
while True:
	# Prompt user to input character data
	print("\nEnter Character Data")
	name = input("Character Name\t: ")
	job = input("Character's Job\t: ")
	level = input("Character Level\t: ")

	# Create a new character entry
	new_character = [name, job, level]
	character_list.append(new_character)

	# Display current list of characters
	print("\n\n","="*10,"Character Data","="*10)
	for index, character in enumerate(character_list):
		print(f"{index+1} | {character[0]} | {character[1]} | Level {character[2]}")
	
	print("\n\n","="*20)
	# Ask if user wants to continue
	proceed = input("Continue?(y/n) ")

	if proceed == "n":
		break

print("PROGRAM COMPLETED")
