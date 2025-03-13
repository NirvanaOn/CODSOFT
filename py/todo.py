import tkinter
from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("400x550+400+100")
root.resizable(False, False)

list = []

def addtask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        list.append(task)
        box.insert(END, task)

def deletetask():
    selected_task = box.curselection()
    if selected_task:
        task = box.get(selected_task)
        list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in list:
                taskfile.write(task + "\n")
        box.delete(selected_task)

def openTaskFile():
    try:
        global list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():
                list.append(task.strip())
                box.insert(END, task.strip())
    except:
        open("tasklist.txt", 'w').close()

title_icon = PhotoImage(file="1.png")
root.iconphoto(False, title_icon)

canvas = Canvas(root, width=400, height=650)
canvas.place(x=0, y=0)

def draw_gradient():
    for i in range(255):
        gray_value = hex(i)[2:].zfill(2)
        color = f"#{gray_value}{gray_value}{gray_value}"
        canvas.create_line(0, i * 2, 400, i * 2, fill=color)

draw_gradient()

frame1 = Frame(root, bg="black", width=400, height=80)
frame1.pack(fill="x")

head = Label(frame1, text="To Do List", bg="black", fg="white", font="Arial 18 bold")
head.place(x=140, y=25)

frame = Frame(root, bg="white", width=400, height=45)
frame.place(x=0, y=120)

taske = StringVar()
task_entry = Entry(frame, textvariable=taske, width=22, font="Arial 16", bd=2, relief=SOLID)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="Arial 14 bold", width=6, bg="black", fg="white", bd=2, relief=SOLID, command=addtask)
button.place(x=315, y=5)

frame2 = Frame(root, bd=3, bg="black", width=400, height=280)
frame2.pack(pady=(160, 0), padx=10)

box = Listbox(frame2, font=('Arial', 12), width=40, height=12, bg="black", fg="white", cursor="hand2", selectbackground="gray")
box.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

delete_button = Button(root, text="DELETE", font="Arial 14 bold", width=10, bg="black", fg="white", bd=2, relief=SOLID, command=deletetask)
delete_button.pack(side=BOTTOM, pady=13)

openTaskFile()

root.mainloop()
