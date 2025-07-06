from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")
class Over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.write("GAME OVER!", align = ALIGN, font = FONT)



