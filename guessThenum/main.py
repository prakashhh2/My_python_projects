import random
import tkinter as tk
from tkinter import messagebox

# Generate a random 4-digit number
secret = str(random.randint(1111, 9999))
print("Guess the 4-digit number!")

# Create Window
root = tk.Tk()
root.title("4-Digit Guessing Game")
root.geometry("350x400")
root.config(bg= "#1c1c1c")

# Game title
title = tk.Label(root, text = "Guess the 4 Digit number!", font=("Arial",16, "bold"), bg = "#1c1c1c", fg ="#00ff7f")
title.pack(pady = 15)

# Input file

entry = tk.Entry(root, font =("Arial", 14), justify="center")
entry.pack(pady=10)

# Display result box

result_box = tk.Text(root,height=10, width=35, font=("consolas", 12) )
result_box.pack(pady= 15)
result_box.config(state="disabled", bg ="#2a2a2a", fg = "white")

# core game logic
def check_guess():
    guess = entry.get().strip()

    if len(guess) != 4 or not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please entre Exactly 4 digits.")
        return
    global secret

    if guess == secret:
        messagebox.showinfo("You win!",f"Correct! The number was{secret}")
        reset_game()
        return
    
    correct_pos = sum(1 for i in range(4) if guess[i] == secret[i])

    # Count correct digits (wrong position)
    correct_digits = 0
    secret_copy = list(secret)
    guess_copy = list(guess)

    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            secret_copy[i] = "_"
            guess_copy[i] = "_"

    for digit in guess_copy:
        if digit != "_" and digit in secret_copy:
            correct_digits += 1
            secret_copy[secret_copy.index(digit)] = "_"

     # Show result in text box
    result_box.config(state="normal")
    result_box.insert(tk.END, f"Guess: {guess} | Pos: {correct_pos}, Wrong Pos: {correct_digits}\n")
    result_box.config(state="disabled")
    result_box.see(tk.END)

    entry.delete(0, tk.END)

def reset_game():
    global secret
    secret = str(random.randint(1111, 9999))
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "New Game Started!\n")
    result_box.config(state="disabled")
    entry.delete(0, tk.END)

# Buttons
btn_frame = tk.Frame(root, bg="#1c1c1c")
btn_frame.pack(pady=10)

check_btn = tk.Button(btn_frame, text="Check", font=("Arial", 12), bg="#00ff7f", fg="black", width=10, command=check_guess)
check_btn.grid(row=0, column=0, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", font=("Arial", 12), bg="#ff4757", fg="white", width=10, command=reset_game)
reset_btn.grid(row=0, column=1, padx=5)

root.mainloop()
    


