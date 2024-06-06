# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Initialize the window
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Greet Them!")

# Variables and Functions
FIRST_NAME = tk.StringVar()
LAST_NAME = tk.StringVar()

def greet_button_click():
    '''Function triggered by the button'''
    message = f"Hello {FIRST_NAME.get()} {LAST_NAME.get()}, Brilliant!"
    showinfo(title="Greetings!", message=message)

# Input frame
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

# Components
# 1. First name label
first_name_label = ttk.Label(input_frame, text="First Name:")
first_name_label.pack(padx=10, fill="x", expand=True)
# 2. First name entry
first_name_entry = ttk.Entry(input_frame, textvariable=FIRST_NAME)
first_name_entry.pack(padx=10, fill="x", expand=True)
# 3. Last name label
last_name_label = ttk.Label(input_frame, text="Last Name:")
last_name_label.pack(padx=10, fill="x", expand=True)
# 4. Last name entry
last_name_entry = ttk.Entry(input_frame, textvariable=LAST_NAME)
last_name_entry.pack(padx=10, fill="x", expand=True)
# 5. Greet button
greet_button = ttk.Button(input_frame, text="Greet!", command=greet_button_click)
greet_button.pack(fill='x', expand=True, padx=10, pady=10)

# Main window loop
window.mainloop()
