import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = []

for i in range(3):
    snake_segment = Turtle("square")
    snake_segment.penup()
    snake_segment.color("white")
    snake_segment.goto(-20 * i, 0)
    snake.append(snake_segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)
    snake[0].forward(20)

screen.exitonclick()
