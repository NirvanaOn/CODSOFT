import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")


tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()


tk.Label(root, text="Select operation:").pack()
operator_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
for op in operations:
    tk.Radiobutton(root, text=op, variable=operator_var, value=op).pack()


tk.Button(root, text="Calculate", command=calculate).pack()


result_label = tk.Label(root, text="Result : ")
result_label.pack()

root.mainloop()
