import tkinter as tk
from tkinter import messagebox
import random

user_score = 0
computer_score = 0

def play(choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Scissors" and computer_choice == "Paper") or \
         (choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1
    
    messagebox.showinfo("Result", f"Your Choice: {choice}\nComputer's Choice: {computer_choice}\n\n{result}")
    update_score()

def update_score():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score()

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Title label
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16)).pack(pady=10)

# Buttons for user choices
tk.Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

# Score labels
user_score_label = tk.Label(root, text="Your Score: 0", font=("Helvetica", 12))
user_score_label.pack(pady=5)
computer_score_label = tk.Label(root, text="Computer's Score: 0", font=("Helvetica", 12))
computer_score_label.pack(pady=5)

# Reset button
tk.Button(root, text="Reset Game", width=15, command=reset_game).pack(pady=10)

# Run the application
root.mainloop()
