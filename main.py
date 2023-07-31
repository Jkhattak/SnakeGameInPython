import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=800, height=800)
screen.bgcolor("green")
screen.tracer(0)

# Create border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("orange")
border_pen.pensize(4)
border_pen.penup()
border_pen.goto(-310, 250)
border_pen.pendown()
for _ in range(2):
    border_pen.forward(620)
    border_pen.right(90)
    border_pen.forward(500)
    border_pen.right(90)
border_pen.hideturtle()

# Score
score = 0

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")  
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 350)
scoring.write("Score: ", align="center", font=("Courier", 24, "bold"))

# Functions for movement
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main game loop
delay = 0.1
old_fruit = []

while True:
    screen.update()

    # Check for collision with food
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # Update score
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))

        # Add a new piece to the snake
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Move the end pieces first in reverse order
    for index in range(len(old_fruit) - 1, 0, -1):
        x = old_fruit[index - 1].xcor()
        y = old_fruit[index - 1].ycor()
        old_fruit[index].goto(x, y)

    # Move the first piece to where the snake's head is
    if len(old_fruit) > 0:
        x = snake.xcor()
        y = snake.ycor()
        old_fruit[0].goto(x, y)

    # Move the snake
    snake_move()

    # Check for collisions with border
    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Reset score and hide old fruit pieces
        score = 0
        scoring.clear()
        for piece in old_fruit:
            piece.goto(1000, 1000)
        old_fruit.clear()

    # Check for collisions with snake's body
    for piece in old_fruit:
        if piece.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"

            # Reset score and hide old fruit pieces
            score = 0
            scoring.clear()
            for piece in old_fruit:
                piece.goto(1000, 1000)
            old_fruit.clear()

    # Pause before the next frame
    time.sleep(delay)

turtle.done()
