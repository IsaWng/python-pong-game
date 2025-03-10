from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.penup()
        self.goto(position)
        self.score = 0

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
