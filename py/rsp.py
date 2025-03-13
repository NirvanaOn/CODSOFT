import tkinter as tk
from tkinter import PhotoImage  
from PIL import Image, ImageTk 
import random

# Initialize window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#121212")  # Dark background like Windows 11 Dark Mode

user_score = 0
computer_score = 0

# Function to update the user's choice image
def updateuser_image(choice):
    img = Image.open(image_paths[choice]).resize((70, 70))  # Bigger images
    user_photo = ImageTk.PhotoImage(img)
    user_label.config(image=user_photo)
    user_label.image = user_photo
    user_label.place(x=50, y=80)

# Function to play the game
def play_game():
    global user_score, computer_score
    user_choice = selectoption.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    img = Image.open(image_paths[computer_choice]).resize((70, 70))
    computer_photo = ImageTk.PhotoImage(img)
    computer_label.config(image=computer_photo)
    computer_label.image = computer_photo
    computer_label.place(x=230, y=80)

    # Determine result
    if user_choice == computer_choice:
        result_text = "🤝 It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text = "🎉 You Win!"
        user_score += 1
    else:
        result_text = "💀 Computer Wins!"
        computer_score += 1

    # Update score
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
    result_label.config(text=result_text)

# Image Paths
image_paths = {"Rock": "stone.png", "Paper": "scroll.png", "Scissors": "scissors.png"}

# Score Label (Glowing Effect)
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), fg="#0df3a3", bg="#121212")
score_label.pack(pady=10)

# User Choice Dropdown
selectoption = tk.StringVar()
selectoption.set("Rock")
dropdown = tk.OptionMenu(root, selectoption, *image_paths.keys(), command=updateuser_image)
dropdown.config(font=("Arial", 12), bg="#222", fg="white", activebackground="#444")
dropdown.place(x=120, y=250)

# User and Computer Image Labels
user_label = tk.Label(root, bg="#121212")
user_label.pack(side="left", padx=20, pady=20)

computer_label = tk.Label(root, bg="#121212")
computer_label.pack(side="right", padx=20, pady=20)

# Set Window Icon
title_icon = PhotoImage(file="rps.png")  
root.iconphoto(False, title_icon)

# Play Button (Modern Look)
play_button = tk.Button(root, text="▶ Play", font=("Arial", 12, "bold"), bg="#0df3a3", fg="black", 
                        activebackground="#00b383", activeforeground="black", padx=10, pady=5, borderwidth=0, relief="flat",
                        command=play_game)
play_button.place(x=140, y=200)

# Result Label (Futuristic Look)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#121212")
result_label.pack(pady=10)

# Initialize default user image
updateuser_image("Rock")

# Run the GUI
root.mainloop()
