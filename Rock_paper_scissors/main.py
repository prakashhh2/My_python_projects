import random
print("This is the Rock Paper Scissor game with computer")
while True:
    com_num = random.randint(1, 3)
    relation = {1: "r", 2: "s", 3: "p"}
    com_choice = relation.get(com_num)

    try:
        my_choice = input("Enter your choice (r/s/p): ").lower()

        if my_choice not in ['r', 's', 'p']:
            raise ValueError  # force error for invalid input

        print(f"Computer chose: {com_choice}")

        if my_choice == com_choice:
            print("😐 Draw!")
        elif (my_choice == 'r' and com_choice == 's') or \
             (my_choice == 'p' and com_choice == 'r') or \
             (my_choice == 's' and com_choice == 'p'):
            print("🔥 You Win!")
        else:
            print("💻 Computer Wins!")

    except ValueError:
        print("❌ Enter a valid input (r/s/p)")

    again = input("Wanna play again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break
