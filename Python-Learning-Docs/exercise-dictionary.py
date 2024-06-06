import datetime
import os
import string
import random

# Template dictionary for student data
student_template = {
    'name': 'name',
    'id_number': '00000000',
    'completed_credits': 0,
    'birthdate': datetime.datetime(1111, 1, 11)
}

student_data = {}

while True:
    os.system("cls")
    print(f"{'WELCOME':^20}")
    print(f"{'STUDENT DATA':^20}")
    print("-" * 20)

    student = dict.fromkeys(student_template.keys())
    student['name'] = input("Student's Name: ")
    student['id_number'] = input("Student's ID Number: ")
    student['completed_credits'] = int(input("Completed Credits: "))
    YEAR_OF_BIRTH = int(input("Year of Birth (YYYY): "))
    MONTH_OF_BIRTH = int(input("Month of Birth (1-12): "))
    DAY_OF_BIRTH = int(input("Day of Birth (1-31): "))
    student['birthdate'] = datetime.datetime(YEAR_OF_BIRTH, MONTH_OF_BIRTH, DAY_OF_BIRTH)

    # Generating a unique key for each student
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    student_data.update({KEY: student})

    # Displaying student data
    print(f"\n{'KEY':<10} {'Name':<17} {'ID Number':<10} {'Credits':<8} {'Birthdate':<11}")
    print('-' * 60)

    for student_key, student_info in student_data.items():
        print(f"{student_key:<10} {student_info['name']:<17} {student_info['id_number']:<10} {student_info['completed_credits']:^8} {student_info['birthdate'].strftime("%x"):^11}")

        print("\n")
    is_done = input("Would you like to add another student? (y/n): ")
    if is_done == "n":
        break

    print("\nEnd of program, thank you!")




