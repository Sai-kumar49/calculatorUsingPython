import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
def button_click(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 14), command=calculate, height=2, width=5)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 14), command=clear_entry, height=2, width=5)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: button_click(t), height=2, width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)
root.mainloop()
