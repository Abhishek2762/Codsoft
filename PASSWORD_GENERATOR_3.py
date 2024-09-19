import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")  # Light grey background
        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_input_frame()
        self.create_generate_button()
        self.create_password_label()

    def create_header(self):
        header_label = tk.Label(self.root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        header_label.pack(pady=10)

    def create_input_frame(self):
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10)

        self.create_length_input(input_frame)
        self.create_character_options(input_frame)

    def create_length_input(self, parent):
        length_label = tk.Label(parent, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
        length_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.length_entry = tk.Entry(parent, font=("Helvetica", 12))
        self.length_entry.grid(row=0, column=1, pady=5, padx=5)

    def create_character_options(self, parent):
        include_label = tk.Label(parent, text="Include:", font=("Helvetica", 12), bg="#f0f0f0")
        include_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")

        self.include_lowercase = tk.BooleanVar()
        self.include_lowercase.set(True)  # Default to include lowercase
        self.create_checkbox(parent, "Lowercase Letters", self.include_lowercase, 2)

        self.include_uppercase = tk.BooleanVar()
        self.create_checkbox(parent, "Uppercase Letters", self.include_uppercase, 3)

        self.include_numbers = tk.BooleanVar()
        self.create_checkbox(parent, "Numbers", self.include_numbers, 4)

        self.include_special = tk.BooleanVar()
        self.create_checkbox(parent, "Special Characters", self.include_special, 5)

    def create_checkbox(self, parent, text, variable, row):
        checkbox = tk.Checkbutton(parent, text=text, variable=variable, font=("Helvetica", 12), bg="#f0f0f0")
        checkbox.grid(row=row, column=0, pady=5, padx=5, sticky="w")

    def create_generate_button(self):
        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="green", fg="white", command=self.generate_password)
        self.generate_button.pack(pady=20)

    def create_password_label(self):
        self.password_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
            return

        length = int(length)
        if length < 8:
            messagebox.showerror("Invalid Input", "Password length must be at least 8.")
            return

        characters = self.get_characters()
        if not characters:
            messagebox.showerror("Invalid Input", "Please select at least one character set.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

    def get_characters(self):
        characters = ""
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_numbers.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation
        return characters

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()