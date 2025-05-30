import tkinter as tk
from tkinter import ttk, messagebox
import random
import string



def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer for length.")

        return

    strength = strength_var.get()

    if strength == "Low":
        chars = string.ascii_lowercase
    elif strength == "Medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)




def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 10), padding=6)
style.configure("TLabel", font=("Helvetica", 11))
style.configure("TEntry", font=("Helvetica", 11))
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)
ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky='w')
length_entry = ttk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, pady=5)
ttk.Label(frame, text="Strength:").grid(row=1, column=0, sticky='w')
strength_var = tk.StringVar(value="Strong")
ttk.Combobox(frame, textvariable=strength_var, values=["Low", "Medium", "Strong"], state='readonly', width=10).grid(row=1, column=1, pady=5)
ttk.Button(frame, text="Generate Password", command=generate).grid(row=2, column=0, columnspan=2, pady=10)
ttk.Label(frame, text="Generated Password:").grid(row=3, column=0, sticky='w')
result_entry = ttk.Entry(frame, width=30)
result_entry.grid(row=3, column=1, pady=5)
ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=4, column=0, columnspan=2, pady=10)



root.mainloop()
