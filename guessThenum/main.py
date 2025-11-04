import random

secret = str(random.randint(1111, 9999))
print("Guess the 4-digit number!")

while True:
    guess = input("Enter your guess: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Please enter exactly 4 digits.")
        continue

    if guess == secret:
        print("🎉 Correct! You guessed the number:", secret)
        break

    # Count correct position
    correct_pos = sum(1 for i in range(4) if guess[i] == secret[i])

    # Count digits that exist in secret (but remove already matched ones)
    correct_digits = 0
    secret_copy = list(secret)
    guess_copy = list(guess)

    # Remove digits already counted as correct position
    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            secret_copy[i] = "_"
            guess_copy[i] = "_"

    # Count correct digits wrong position
    for digit in guess_copy:
        if digit != "_" and digit in secret_copy:
            correct_digits += 1
            secret_copy[secret_copy.index(digit)] = "_"

    print(f"Correct position: {correct_pos},  Correct digit wrong position: {correct_digits}")
