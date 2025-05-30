import tkinter as tk
from tkinter import ttk
import math

def evaluate():
    try:
        expr = entry.get()
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



def click(btn):
    entry.insert(tk.END, btn)


def clear():
    entry.delete(0, tk.END)

def create_button(text, row, col, width=6, colspan=1):
    style = 'Hover.TButton'
    b = ttk.Button(root, text=text, style=style, width=width, command=lambda: evaluate() if text == '=' else (clear() if text == 'C' else click(text)))
    b.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky='nsew')




root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.resizable(False, False)
style = ttk.Style(root)
style.configure("TButton", font=('Helvetica', 12), padding=5)
style.configure("Hover.TButton", font=('Helvetica', 12), padding=5, relief="flat", background="#e0e0e0")
style.map("Hover.TButton", background=[("active", "#d0d0d0")])
entry = tk.Entry(root, font=('Helvetica', 20), justify='right', bd=10, relief=tk.FLAT)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
buttons = [
    ['7', '8', '9', '/', 'sin(', 'cos('],
    ['4', '5', '6', '*', 'tan(', 'log('],
    ['1', '2', '3', '-', 'sqrt(', 'exp('],
    ['0', '.', '(', ')', '+', '^'],
    ['pi', 'e', 'C', '=', '', '']
]
for i, row_vals in enumerate(buttons):
    for j, val in enumerate(row_vals):
        if val:
            if val == '^':
                create_button("**", i+1, j)
            elif val == 'pi':
                create_button("math.pi", i+1, j)
            elif val == 'e':
                create_button("math.e", i+1, j)
            else:
                create_button(val, i+1, j)





for i in range(6):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i, weight=1)



root.mainloop()
