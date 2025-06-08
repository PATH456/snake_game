from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_over import Over
from food_timer import Timer
import time
import random
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
game_start = True
big_food = False
screen = Screen()
screen.setup(width= 1500, height= 1500)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()
my_timer = Timer()
def up():
    if my_snake.first_segment.heading() != DOWN:
        my_snake.first_segment.setheading(90)
def down():
    if my_snake.first_segment.heading() != UP:
        my_snake.first_segment.setheading(270)
def left():
    if my_snake.first_segment.heading() != RIGHT:
        my_snake.first_segment.setheading(180)
def right():
    if my_snake.first_segment.heading() != LEFT:
        my_snake.first_segment.setheading(0)

screen.listen()
screen.onkey(fun= left, key= "Left")
screen.onkey(fun= right, key = "Right")
screen.onkey(fun= up, key= "Up")
screen.onkey(fun= down, key= "Down")

while game_start:
    pos_list = []
    for segment in my_snake.segment_list:
        pos_list.append(segment.position())
    while my_food.position() in pos_list:
        my_food.refresh()
    screen.update()
    time.sleep(0.05)
    my_snake.move()
    if my_food.refresh_count % 8 == 0:
        my_food.shapesize(stretch_len=2, stretch_wid=2)
        if not big_food:
            my_timer.time = 5
            my_timer.countdown(screen)
            big_food = True
        if my_timer.time == 0:
            my_food.refresh()
            my_food.shapesize(stretch_len=0.5, stretch_wid=0.5)
            big_food = False
        if my_snake.first_segment.distance(my_food) < 20:
            my_food.refresh()
            for extend in range(3):
                my_snake.extend()
            my_score.clear_score()
            my_score.score += random.randint(4, 10)
            my_score.score_update()
    else:
        my_timer.time = 0
        big_food = False
        my_food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        if my_snake.first_segment.distance(my_food) < 20:
            my_food.refresh()
            my_snake.extend()
            my_score.clear_score()
            my_score.score_update()
    if int(my_snake.first_segment.xcor()) > 750:
        my_snake.first_segment.setx(-750)
    elif int(my_snake.first_segment.xcor()) < -750:
        my_snake.first_segment.setx(750)
    elif int(my_snake.first_segment.ycor()) > 750:
        my_snake.first_segment.sety(-750)
    elif int(my_snake.first_segment.ycor()) < -750:
        my_snake.first_segment.sety(750)

    for segment in my_snake.segment_list[1:]:
        if my_snake.first_segment.distance(segment) < 10:
            game_start = False
            game_over = Over()




screen.exitonclick()





















screen.exitonclick()












