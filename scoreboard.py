from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 700)
        self.score_update()

    def score_update(self):
        self.write(f"SCORE: {self.score}  HIGHSCORE: {self.high_score}", align= ALIGN, font=FONT)
        self.score += 1

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def clear_score(self):
        self.clear()
