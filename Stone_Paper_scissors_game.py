import tkinter as tk
import random

# Scores
hscore = 0
cscore = 0

# Function to play game
def play(user_choice):
    global hscore, cscore

    com = random.randint(1, 3)

    # Mapping numbers to names
    choices = {1: "Stone", 2: "Paper", 3: "Scissors"}

    user_label.config(text=f"You chose: {choices[user_choice]}")
    comp_label.config(text=f"Computer chose: {choices[com]}")

    # Game logic
    if user_choice == com:
        result = "Draw 😐"

    elif (user_choice == 1 and com == 3) or \
         (user_choice == 2 and com == 1) or \
         (user_choice == 3 and com == 2):
        hscore += 1
        result = "You won this round 🎉"

    else:
        cscore += 1
        result = "Computer won this round 😈"

    result_label.config(text=result)
    score_label.config(text=f"You: {hscore}  |  Computer: {cscore}")

    # Check winner
    if hscore == 5:
        result_label.config(text="🏆 You won the Game!")
        disable_buttons()

    elif cscore == 5:
        result_label.config(text="💀 Computer won the Game!")
        disable_buttons()


# Disable buttons after game ends
def disable_buttons():
    btn_stone.config(state="disabled")
    btn_paper.config(state="disabled")
    btn_scissor.config(state="disabled")


# Reset game
def reset_game():
    global hscore, cscore
    hscore = 0
    cscore = 0

    score_label.config(text="You: 0  |  Computer: 0")
    result_label.config(text="")
    user_label.config(text="")
    comp_label.config(text="")

    btn_stone.config(state="normal")
    btn_paper.config(state="normal")
    btn_scissor.config(state="normal")


# UI Setup
root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.geometry("400x400")

# Title
title = tk.Label(root, text="Stone Paper Scissors", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Score
score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# User & Computer choices
user_label = tk.Label(root, text="", font=("Arial", 11))
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 11))
comp_label.pack()

# Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

btn_stone = tk.Button(btn_frame, text="Stone 🪨", width=10, command=lambda: play(1))
btn_stone.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(btn_frame, text="Paper 📄", width=10, command=lambda: play(2))
btn_paper.grid(row=0, column=1, padx=5)

btn_scissor = tk.Button(btn_frame, text="Scissors ✂️", width=10, command=lambda: play(3))
btn_scissor.grid(row=0, column=2, padx=5)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

# Run app
root.mainloop()