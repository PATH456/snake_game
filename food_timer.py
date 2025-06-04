from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")
class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.time = 5
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, -740)

    def time_update(self):
        self.clear()
        self.write(f"TIME: {self.time}", align=ALIGN, font=FONT)
        self.time -= 1

    def countdown(self, screen):
        if self.time > 0:
            self.time_update()
            screen.ontimer(lambda: self.countdown(screen), 1000)
        else:
            self.clear()
            self.time -= 1








