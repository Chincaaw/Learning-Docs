# string Width and Multiline

# Data
name_data = "Welt Yang"
age_data = 75
height_data = 190.1
shoe_size_data = 44

# Standard string
standard_string = f"name = {name_data}, age = {age_data}, height = {height_data}, shoe size = {shoe_size_data}"
print(5 * "=" + " Standard String " + 5 * "=")
print(standard_string)

# Multiline string (using newline \n)
multiline_string = f"name = {name_data}, \nage = {age_data}, \nheight = {height_data}, \nshoe size = {shoe_size_data}"
print("\n" + 5 * "=" + " Multiline String " + 5 * "=")
print(multiline_string)

# Multiline string (using triple quotes)
multiline_string = f"""name = {name_data}
age = {age_data}
height = {height_data}
shoe size = {shoe_size_data}
"""
print("\n" + 5 * "=" + " Multiline String " + 5 * "=")
print(multiline_string)

# Adjusting width
name_data = "Ucup Surucup"
height_data = 105.17
formatted_string = f"""
name       = {name_data:>12}
age        = {age_data:>12}
height     = {height_data:>12.2f}
shoe size  = {shoe_size_data:>12}
"""
print("\n" + 5 * "=" + " Formatted String " + 5 * "=")
print(formatted_string)
