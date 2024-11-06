
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tris")

current_player = 1
board = [0] * 9


winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_winner():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != 0:
            return True
    return False


def check_draw():
    return all(cell != 0 for cell in board)


def minimax(board_state, depth, is_maximizing):
    if check_winner():
        return -10 if is_maximizing else 10
    elif check_draw():
        return 0

    available_moves = [i for i, cell in enumerate(board_state) if cell == 0]

    if is_maximizing:
        best_score = -9999
        for move in available_moves:
            board_state[move] = -1
            score = minimax(board_state, depth + 1, False)
            board_state[move] = 0
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 9999
        for move in available_moves:
            board_state[move] = 1
            score = minimax(board_state, depth + 1, True)
            board_state[move] = 0
            best_score = min(score, best_score)
        return best_score


def get_best_move():
    available_moves = [i for i, cell in enumerate(board) if cell == 0]
    best_move = -1
    best_score = -9999

    for move in available_moves:
        board[move] = -1
        score = minimax(board, 0, False)
        board[move] = 0

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def on_click(index):
    global current_player
    if board[index] != 0:
        return

    board[index] = current_player
    buttons[index].config(text="X" if current_player == 1 else "O")

    if check_winner():
        messagebox.showinfo("Game Over", f"Player {'X' if current_player == 1 else 'O'} wins!")
        reset_board()
        return
    elif check_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()
        return

    current_player = -1 if current_player == 1 else 1
    if current_player == -1:
        bot_move = get_best_move()
        board[bot_move] = current_player
        buttons[bot_move].config(text="O")
        if check_winner():
            messagebox.showinfo("Game Over", "Player O wins!")
            reset_board()
            return
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return
        current_player = 1


def reset_board():
    global board, current_player
    board = [0] * 9
    current_player = 1
    for button in buttons:
        button.config(text="")


buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)


root.mainloop()

