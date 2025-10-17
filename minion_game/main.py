# minion_game.py
import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

VOWELS = 'AEIOU'

def calculate_scores(word):
    """Calculate Kevin and Stuart's scores."""
    kevin_score = 0
    stuart_score = 0
    length = len(word)

    for i in range(length):
        if word[i] in VOWELS:
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)
    
    return kevin_score, stuart_score


def play_game(player1, player2, word):
    """Play the Minion Game."""
    word = word.upper()
    print(Fore.CYAN + f"\nThe word is: {word}\n" + Style.RESET_ALL)

    kevin_score, stuart_score = calculate_scores(word)

    print(Fore.YELLOW + f"{player1}'s Score (Vowels): {kevin_score}")
    print(Fore.GREEN + f"{player2}'s Score (Consonants): {stuart_score}\n")

    if kevin_score > stuart_score:
        winner = player1
    elif stuart_score > kevin_score:
        winner = player2
    else:
        winner = "Draw"

    print(Fore.MAGENTA + f"🏆 Winner: {winner} 🏆\n")

    save_scoreboard(player1, player2, word, kevin_score, stuart_score, winner)


def save_scoreboard(player1, player2, word, kevin_score, stuart_score, winner):
    """Save results to a scoreboard file."""
    with open("scoreboard.txt", "a") as file:
        file.write(f"{player1} vs {player2} | Word: {word} | {player1}: {kevin_score}, {player2}: {stuart_score} | Winner: {winner}\n")


def random_word():
    """Generate a random word."""
    return ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 8)))


if __name__ == "__main__":
    print(Fore.BLUE + "\n✨ Welcome to The Minion Game! ✨" + Style.RESET_ALL)
    player1 = input("Enter name for Player 1 (Vowels): ").capitalize() or "Kevin"
    player2 = input("Enter name for Player 2 (Consonants): ").capitalize() or "Stuart"

    choice = input("\nDo you want to play with a random word? (y/n): ").lower()
    if choice == 'y':
        word = random_word()
    else:
        word = input("Enter your word: ").strip().upper()

    play_game(player1, player2, word)

    print(Fore.LIGHTBLACK_EX + "\nGame record saved in 'scoreboard.txt' 📄")
