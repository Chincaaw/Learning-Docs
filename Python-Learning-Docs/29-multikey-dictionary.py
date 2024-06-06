import datetime

# Define student information dictionaries
harry = {
    'name': 'Harry Potter',
    'student_id': '19022001',
    'credits_completed': 130,
    'scholarship': False,
    'birthdate': datetime.datetime(1980, 7, 31)
}

hermione = {
    'name': 'Hermione Granger',
    'student_id': '19022002',
    'credits_completed': 140,
    'scholarship': True,
    'birthdate': datetime.datetime(1979, 9, 19)
}

ron = {
    'name': 'Ron Weasley',
    'student_id': '19022003',
    'credits_completed': 100,
    'scholarship': False,
    'birthdate': datetime.datetime(1980, 3, 1)
}

# Store student information in a dictionary
students_data = {
    'STU001': harry,
    'STU002': hermione,
    'STU003': ron
}

print(f"{'KEY':<6} {'Name':<20} {'ID':<10} {'Credits':<10} {'Scholarship':<15} {'Birthdate':<10}")
print("-"*80)

for students in students_data:
	KEY = students

	NAME = students_data[KEY]['name']
	ID = students_data[KEY]['student_id']
	CREDITS = students_data[KEY]['credits_completed']
	SCHOLARSHIP = students_data[KEY]['scholarship']
	BIRTHDATE = students_data[KEY]['birthdate'].strftime("%x")

	print(f"{KEY:<6} {NAME:<20} {ID:<10} {CREDITS:<10} {SCHOLARSHIP:<15} {BIRTHDATE:<10}")