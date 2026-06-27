import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("400x450")
window.resizable(False, False)

# Variables
current_player = "X"
board = [""] * 9
buttons = []


# Check winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Draw"

    return None


# Restart Game
def restart_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="", state="normal")

    status.config(text="Player X's Turn")


# Button Click
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        result = check_winner()

        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a Draw!")
            restart_game()

        elif result:
            messagebox.showinfo("Winner", f"Player {result} Wins!")
            restart_game()

        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

            status.config(text=f"Player {current_player}'s Turn")


# Title
title = tk.Label(
    window,
    text="TIC TAC TOE",
    font=("Arial", 22, "bold")
)
title.pack(pady=10)

# Status Label
status = tk.Label(
    window,
    text="Player X's Turn",
    font=("Arial", 16)
)
status.pack()

# Frame
frame = tk.Frame(window)
frame.pack(pady=20)

# Create 9 Buttons
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 14),
    command=restart_game
)

restart_btn.pack(pady=10)

window.mainloop()