# Original data lists
data_list_0 = [1, 2]
data_list_1 = [3, 4, 5]

# Regular list
regular_list = [1, 2, 3, 4]

print(f"Regular list = {regular_list}")

# 2D list
two_dimensional_list = [data_list_0, data_list_1, 6, 7]

print(f"2D list = {two_dimensional_list}")

# Example usage

participant_0 = ["John", 25, "Male"]
participant_1 = ["Doe", 30, "Male"]
participant_2 = ["Jane", 35, "Female"]

participants_list = [participant_0, participant_1, participant_2]

print(f"Participants = {participants_list}")

for participant in participants_list:
    print(f"Name\t: {participant[0]}")
    print(f"Age\t: {participant[1]}")
    print(f"Gender\t: {participant[2]}\n")

# Using reference

participants_copy = participants_list.copy()
print(f"Participants = {participants_copy}")

participant_0[0] = "Michael"
print(f"Participants = {participants_copy}")
print(f"Participants = {participants_list}")
