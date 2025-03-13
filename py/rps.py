import tkinter as tk
from tkinter import PhotoImage  
from PIL import Image, ImageTk 
import random

root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("280x250")
root.resizable(False, False)
root.configure(bg="black") 

user_score = 0
computer_score = 0

def updateuser_image(choice):
    img = Image.open(image_paths[choice]).resize((50, 50)) 
    user_photo = ImageTk.PhotoImage(img)  
    user_label.config(image=user_photo)  
    user_label.image = user_photo 
    user_label.place(x=40, y=90) 
    
def play_game():
    global user_score, computer_score
    user_choice = selectoption.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    img = Image.open(image_paths[computer_choice]).resize((50, 50)) 
    user_photo = ImageTk.PhotoImage(img)  
    computer_label.config(image=user_photo)  
    computer_label.image = user_photo 
    computer_label.place(x=185, y=90) 
    
    result_text = ""
    if user_choice == computer_choice:
        result_text = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text = "You Win!"
        user_score += 1
    else:
        result_text = "Computer Wins!"
        computer_score += 1

 
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    result_label.config(text=result_text)
    
    
image_paths = {"Rock": "stone.png", "Paper": "scroll.png", "Scissors": "scissors.png"}

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 10))
score_label.pack(pady=10)


selectoption =tk.StringVar()
selectoption.set("Rock")
dropdown = tk.OptionMenu(root, selectoption, *image_paths.keys(), command=updateuser_image)
dropdown.place(x=100,y=200)

user_label = tk.Label(root)
user_label.pack(side="left", padx=20, pady=20)

computer_label = tk.Label(root)
computer_label.pack(side="right", padx=20, pady=20)

title_icon = PhotoImage(file="rps.png")  
root.iconphoto(False, title_icon)


play_button = tk.Button(root, text="Play", font=("Arial", 10), command=play_game)
play_button.place(x=120,y=150)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

updateuser_image("Rock")
root.mainloop()
