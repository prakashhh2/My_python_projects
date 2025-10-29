from tkinter import *
import random
import os

# Game settings
GAME_WIDTH = 800
GAME_HEIGHT = 800
START_SPEED = 120
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
SNAKE_HEAD_COLOUR = "#66FF66"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"

highscore_file = "highscore.txt"
if os.path.exists(highscore_file):
    with open(highscore_file, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0


class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        start_x = GAME_WIDTH // 2
        start_y = GAME_HEIGHT // 2

        for i in range(BODY_PARTS):
            self.coordinates.append([start_x - i*SPACE_SIZE, start_y])

        for i, (x, y) in enumerate(self.coordinates):
            color = SNAKE_HEAD_COLOUR if i == 0 else SNAKE_COLOUR
            square = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=color, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        self.oval = self.canvas.create_oval(
            x + 5, y + 5, x + SPACE_SIZE - 5, y + SPACE_SIZE - 5,
            fill=FOOD_COLOUR, tag="food"
        )


def next_turn():
    global snake, food, direction, score, speed, is_paused

    if is_paused:
        window.after(100, next_turn)
        return

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    new_head = [x, y]
    snake.coordinates.insert(0, new_head)

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                     fill=SNAKE_HEAD_COLOUR, tag="snake")
    snake.squares.insert(0, square)

    # Recolor old head to body color
    if len(snake.squares) > 1:
        canvas.itemconfig(snake.squares[1], fill=SNAKE_COLOUR)

    # Wall collision
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return

    # Self collision
    if new_head in snake.coordinates[1:]:
        game_over()
        return

    # Food collision
    if new_head == food.coordinates:
        score += 1
        speed = max(50, speed - 2)  # Speed up
        label.config(text=f"Score: {score}  High Score: {high_score}")
        canvas.delete(food.oval)
        food = Food(canvas)
    else:
        # Remove tail
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.coordinates[-1]

    window.after(speed, next_turn)


def change_direction(new_direction):
    global direction

    opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_direction != opposite.get(direction):
        direction = new_direction


def toggle_pause(event=None):
    global is_paused
    is_paused = not is_paused


def restart(event=None):
    global snake, food, score, direction, speed, is_paused

    canvas.delete("all")
    score = 0
    direction = "down"
    speed = START_SPEED
    is_paused = False
    label.config(text=f"Score: {score}  High Score: {high_score}")

    snake = Snake(canvas)
    food = Food(canvas)

    next_turn()


def game_over():
    global high_score, score

    if score > high_score:
        high_score = score
        with open(highscore_file, "w") as f:
            f.write(str(high_score))

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2,
        text=f"GAME OVER\nScore: {score}",
        fill="white",
        font=('consolas', 50),
        justify=CENTER
    )

    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 + 100,
        text="Press R to Restart",
        fill="yellow",
        font=('consolas', 35)
    )


# Tkinter setup
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"
speed = START_SPEED
is_paused = False

label = Label(window, text=f"Score: {score}  High Score: {high_score}", font=('consolas', 35))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Center the window
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+"
                f"{(window.winfo_screenwidth()//2)-(window.winfo_width()//2)}+"
                f"{(window.winfo_screenheight()//2)-(window.winfo_height()//2)}")

# Controls
window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))
window.bind('p', toggle_pause)
window.bind('P', toggle_pause)
window.bind('r', restart)
window.bind('R', restart)

snake = Snake(canvas)
food = Food(canvas)

next_turn()
window.mainloop()
