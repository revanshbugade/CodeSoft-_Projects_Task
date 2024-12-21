import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    """Generate a random password based on user input."""
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        # Define possible characters for the password
        characters = string.ascii_lowercase
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_digits.get():
            characters += string.digits
        if var_special_chars.get():
            characters += string.punctuation

        # Generate the password
        password = ''.join(random.choices(characters, k=length))
        
        # Display the password in a message box
        messagebox.showinfo("Generated Password", f"Your password is: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length.")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

var_uppercase = tk.BooleanVar(value=True)
check_uppercase = tk.Checkbutton(root, text="Include uppercase letters", variable=var_uppercase)
check_uppercase.pack(anchor='w', padx=20)

var_digits = tk.BooleanVar(value=True)
check_digits = tk.Checkbutton(root, text="Include digits", variable=var_digits)
check_digits.pack(anchor='w', padx=30)

var_special_chars = tk.BooleanVar(value=True)
check_special_chars = tk.Checkbutton(root, text="Include special characters", variable=var_special_chars)
check_special_chars.pack(anchor='w', padx=30)

# Generate button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Run the application
root.mainloop()
