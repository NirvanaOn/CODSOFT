import tkinter as tk
from tkinter import messagebox
import random
import string
import qrcode
import pyperclip


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")
root.resizable(False,False)

def genpas():
    try:
        length = int(password_length.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0")
        all = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(all) for _ in range(length))
        password_display.delete(0,tk.END)
        password_display.insert(0,password)
    except ValueError:
        messagebox.showinfo("Length Error","Enter Correct Length ")
        
def genqracopy():
    password = password_display.get()
    if password:
        pyperclip.copy(password)
        passqr = qrcode.make(password)
        passqr.save("Password.png")
        messagebox.showinfo("Info", "Password Copy And QR Generated ")
        password_display.delete(0,tk.END)
        password_length.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning", "No password generated!")
        


tk.Label(root,text="Enter Length of Password : ").place(x=30,y=28)
password_length = tk.Entry(root,width=10)
password_length.place(x=185,y=30)

gen_button = tk.Button(root,text="Generate Password",command=genpas)
gen_button.place(x=95,y=80)

password_display = tk.Entry(root,width=25)
password_display.place(x=72.5,y=120)

gen_qr= tk.Button(root,text="Generate QR & Copy Password",command=genqracopy)
gen_qr.place(x=60,y=160)

root.mainloop()