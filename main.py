from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


for i in range(3):
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.goto(-20 * i, 0)



screen.exitonclick()
