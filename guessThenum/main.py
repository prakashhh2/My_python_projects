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
    


while True:
    guess = input("Enter your guess: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Please enter exactly 4 digits.")
        continue

    if guess == secret:
        print("🎉 Correct! You guessed the number:", secret)
        break

    # Step 1: Count digits in the correct position
    correct_pos = sum(1 for i in range(4) if guess[i] == secret[i])

    # Step 2: Count correct digits ignoring position
    # Create copies to avoid double counting
    secret_copy = list(secret)
    guess_copy = list(guess)

    # Remove already matched digits (correct positions)
    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            secret_copy[i] = guess_copy[i] = "_"

    # Count digits correct but in wrong position
    correct_digit_wrong_pos = 0
    for digit in guess_copy:
        if digit != "_" and digit in secret_copy:
            correct_digit_wrong_pos += 1
            secret_copy[secret_copy.index(digit)] = "_"

    print(f"Digits correct and in correct position: {correct_pos}")
    print(f"Digits correct but in wrong position: {correct_digit_wrong_pos}")
