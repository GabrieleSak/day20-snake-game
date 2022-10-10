from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(-20 * i, 0)
            self.snake.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
