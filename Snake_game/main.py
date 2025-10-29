from tkinter import *
import random

# Game settings
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 120
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"


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

        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOUR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        self.oval = self.canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOUR, tag="food"
        )


def next_turn(snake, food):
    global direction, score, SPEED

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square)

    # Collision with wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return

    # Collision with self
    if [x, y] in snake.coordinates[1:]:
        game_over()
        return

    # Check food collision
    if [x, y] == food.coordinates:
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete(food.oval)
        food = Food(canvas)
    else:
        # Delete last part of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, lambda: next_turn(snake, food))


def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2,
        text=f"GAME OVER\nScore: {score}",
        fill="white",
        font=('consolas', 50),
        justify=CENTER
    )


# Tkinter setup
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text=f"Score: {score}", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Controls
window.bind('<Left>', lambda e: change_direction('left'))
window.bind('<Right>', lambda e: change_direction('right'))
window.bind('<Up>', lambda e: change_direction('up'))
window.bind('<Down>', lambda e: change_direction('down'))

snake = Snake(canvas)
food = Food(canvas)

next_turn(snake, food)

window.mainloop()
