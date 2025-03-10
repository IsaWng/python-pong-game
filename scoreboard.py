from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}   ", font=("Arial", 40, "normal"), align="center")
        self.goto(100, 220)
        self.write(f"{self.r_score}   ", font=("Arial", 40, "normal"), align="center")
