import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    score_label.config(text=f"User: {user_score}  Computer: {computer_score}")

def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_score(result)

def play_again():
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        result_label.config(text="")
    else:
        root.quit()

root = tk.Tk()
root.title("Rock, Paper, Scissors")

user_score = 0
computer_score = 0

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 14))
instruction_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: [play_game("Rock"), play_again()])
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: [play_game("Paper"), play_again()])
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: [play_game("Scissors"), play_again()])
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"User: {user_score}  Computer: {computer_score}", font=("Helvetica", 14))
score_label.pack(pady=20)

root.mainloop()
