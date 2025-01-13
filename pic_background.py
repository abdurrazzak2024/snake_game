import tkinter
import random

ROWS = 24
COLS = 24
TITLE_SIZE = 24
WINDOW_WIDTH = TITLE_SIZE * ROWS
WINDOW_HEIGHT = TITLE_SIZE * COLS


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Initialize the main window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Center the window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (WINDOW_WIDTH / 2))
window_y = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{window_x}+{window_y}")

# Initialize the snake and food
snake = Tile(15 * TITLE_SIZE, 15 * TITLE_SIZE)
food = Tile(10 * TITLE_SIZE, 10 * TITLE_SIZE)
snake_body = []

velocityx = 0
velocityy = 0
game_over = False
score = 0

def change_direction(e):
    global velocityx, velocityy,game_over
    if(game_over):
        return 

    if e.keysym == "Up" and velocityy != 1:
        velocityx = 0
        velocityy = -1
    elif e.keysym == "Down" and velocityy != -1:
        velocityx = 0
        velocityy = 1
    elif e.keysym == "Left" and velocityx != 1:
        velocityx = -1
        velocityy = 0
    elif e.keysym == "Right" and velocityx != -1:
        velocityx = 1
        velocityy = 0


def move():
    global snake,food, snake_body,game_over,score
    if(game_over):
        return 
    if(snake.x < 0 or snake.x >=WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    
    for tile in snake_body:
        if(snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TITLE_SIZE
        food.y = random.randint(0, ROWS - 1) * TITLE_SIZE
        score += 1

    #update snake body
    for i in range(len(snake_body)-1,-1,-1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y



    snake.x += velocityx * TITLE_SIZE
    snake.y += velocityy * TITLE_SIZE


def draw():
    global snake, food,snake_body,game_over,score

    move()

    # Clear the canvas
    canvas.delete("all")

    # Draw the snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TITLE_SIZE, snake.y + TITLE_SIZE, fill="lime green")

    # Draw the food
    canvas.create_rectangle(food.x, food.y, food.x + TITLE_SIZE, food.y + TITLE_SIZE, fill="red")

    # Draw the snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TITLE_SIZE, tile.y + TITLE_SIZE, fill="lime green")
      
    if(game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2,font = "Arial 20", text = f"Game Over sad maruf you should more cleaver:{score}",fill = "white")
    else:
        canvas.create_text(30,20, font = "Arial 10",text = f"Score:{score}",fill = "white")
    # Schedule the next draw call
    window.after(100, draw)


# Corrected binding for key press events
window.bind("<KeyPress>", change_direction)

draw()
window.mainloop()


