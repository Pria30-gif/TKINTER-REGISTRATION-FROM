import tkinter as tk
from tkinter import messagebox, ttk
import re

# Validation and submit function
def submit_form():
    # Get all input values
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()
    phone = entry_phone.get().strip()
    password = entry_password.get().strip()
    gender = gender_var.get()
    country = country_var.get()

    # Reset field colors to normal
    reset_field_colors()

    # Validation checks
    if not name:
        highlight_error(entry_name, "Name cannot be empty.")
        return

    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        highlight_error(entry_email, "Enter a valid email address.")
        return

    if not age.isdigit() or int(age) <= 0:
        highlight_error(entry_age, "Age must be a positive number.")
        return

    if not phone.isdigit() or len(phone) != 10:
        highlight_error(entry_phone, "Phone must be 10 digits.")
        return

    if len(password) < 6:
        highlight_error(entry_password, "Password must be at least 6 characters.")
        return

    # If all inputs are valid
    messagebox.showinfo("Success", f"Registration Completed!\n\nWelcome {name} from {country}.")

# Highlight a field in red and show an error message
def highlight_error(entry_widget, message):
    entry_widget.delete(0, tk.END)  # clear invalid entry
    entry_widget.config(bg="#ffcccc")  # highlight in red
    messagebox.showwarning("Validation Error", message)

# Reset all field background colors
def reset_field_colors():
    for entry in [entry_name, entry_email, entry_age, entry_phone, entry_password]:
        entry.config(bg="white")

# Main window
root = tk.Tk()
root.title("Registration Form with Validation")
root.geometry("480x550")
root.configure(bg="#f0f4f7")

# Title
tk.Label(root, text="Registration Form", font=("Helvetica", 20, "bold"), fg="#333", bg="#f0f4f7").pack(pady=20)

# Form Frame
form_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
form_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Helper to create fields
def add_field(row, label_text, entry_widget):
    tk.Label(form_frame, text=label_text, font=("Helvetica", 12), bg="#ffffff").grid(row=row, column=0, sticky="w", padx=20, pady=10)
    entry_widget.grid(row=row, column=1, padx=20, pady=10)

# Name
entry_name = tk.Entry(form_frame, font=("Helvetica", 11), width=30)
add_field(0, "Name:", entry_name)

# Email
entry_email = tk.Entry(form_frame, font=("Helvetica", 11), width=30)
add_field(1, "Email:", entry_email)

# Age
entry_age = tk.Entry(form_frame, font=("Helvetica", 11), width=30)
add_field(2, "Age:", entry_age)

# Phone
entry_phone = tk.Entry(form_frame, font=("Helvetica", 11), width=30)
add_field(3, "Phone:", entry_phone)

# Password
entry_password = tk.Entry(form_frame, font=("Helvetica", 11), width=30, show='*')
add_field(4, "Password:", entry_password)

# Gender
tk.Label(form_frame, text="Gender:", font=("Helvetica", 12), bg="#ffffff").grid(row=5, column=0, sticky="w", padx=20, pady=10)
gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(form_frame, bg="#ffffff")
gender_frame.grid(row=5, column=1, pady=10, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#ffffff").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#ffffff").pack(side="left", padx=10)

# Country
tk.Label(form_frame, text="Country:", font=("Helvetica", 12), bg="#ffffff").grid(row=6, column=0, sticky="w", padx=20, pady=10)
country_var = tk.StringVar()
country_combo = ttk.Combobox(form_frame, textvariable=country_var, values=["India", "USA", "UK", "Australia", "Canada"], font=("Helvetica", 11), width=27)
country_combo.grid(row=6, column=1, pady=10)
country_combo.set("India")

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="white", font=("Helvetica", 13), width=15)
submit_btn.pack(pady=20)

# Run the GUI
root.mainloop()
