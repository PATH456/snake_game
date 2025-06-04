from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.refresh_count = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color("white")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-740, 740)
        random_y = random.randint(-740, 720)
        self.goto(random_x, random_y)
        self.refresh_count += 1









