import datetime as dt

# Input date of birth
print("Enter your date of birth.")
date = int(input("date (dd): "))
month = int(input("month (mm): "))
year = int(input("year (yyyy): "))

# Convert input to a datetime object
dob = dt.date(year, month, date)

current_date = dt.date.today()

# Calculating age
age = current_date - dob

# Extraction of year, month, and day from age
years = age.days // 365
remaining_days = age.days % 365
months = remaining_days // 30
days = remaining_days % 30

# Displays age
print(f"Umur Anda sekarang adalah {years} tahun, {months} bulan, dan {days} hari.") # I think this is not very accurate considering that there are some months that don't even have 30 days