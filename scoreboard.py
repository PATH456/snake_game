from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 700)
        self.score_update()

    def score_update(self):
        self.write(f"SCORE: {self.score}", align= ALIGN, font=FONT)
        self.score += 1

    def clear_score(self):
        self.clear()
