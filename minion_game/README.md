# 🧠 The Minion Game – Python Edition  

Welcome to **The Minion Game**, a fun and strategic word-based challenge between two players — **Kevin** and **Stuart** — inspired by the famous HackerRank problem.  
This version transforms that coding challenge into a **fully interactive Python project** with color-coded gameplay, automatic scoring, and a saved scoreboard.  

---

## 🎮 Game Concept  

In this game, both players are given the **same word**, and they earn points based on all possible substrings that can be made from it.  

- **Kevin’s rule:** He scores points for all substrings that start with a **vowel** (A, E, I, O, U).  
- **Stuart’s rule:** He scores points for all substrings that start with a **consonant** (any letter other than vowels).  

The number of points is determined by how many times a substring appears in the original word.  
This concept tests your understanding of **string manipulation, loops, and substring generation** in Python — while turning it into an actual playable game!

---

## 🧩 Game Logic Explained  

If the given string is `"BANANA"`:
- Kevin gets points for substrings starting with vowels: `A`, `AN`, `ANA`, etc.
- Stuart gets points for substrings starting with consonants: `B`, `BA`, `BAN`, etc.

Instead of generating all substrings (which would be slow), we use an optimized approach:  
Every letter contributes `(len(string) - index)` possible substrings.  

Example: Word = BANANA
Length = 6

At index 1 (`A`), Kevin gets `6 - 1 = 5` points.  
At index 2 (`N`), Stuart gets `6 - 2 = 4` points.  
And so on...  

This logic gives **O(n)** efficiency — much faster than brute force substring generation!

---

## ⚙️ Tech & Python Concepts Used  

- **String slicing** and **index-based substring calculation**  
- **Loop optimization (O(n))**  
- **Conditional logic** for vowel vs consonant scoring  
- **File handling** (`scoreboard.txt` for game history)  
- **Terminal color output** using the `colorama` library  
- **Random word generation** with the `random` and `string` modules  

---

## 🚀 How to Play  

### 🧱 1. Run the Game  
```bash
python3 minion_game.py
```

## You can see the score after runing the game
[Scoreboard](/MY_PYTHON_PROJECTS/scoreboard.txt)



