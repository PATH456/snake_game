from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_over import Over
import time
import random
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
game_start = True
screen = Screen()
screen.setup(width= 1500, height= 1500)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score = Scoreboard()
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
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    if my_snake.first_segment.distance(my_food) < 20:
        my_food.refresh()
        my_snake.extend()
        my_score.clear_score()
        my_score.score_update()
    if int(my_snake.first_segment.xcor()) > 750 or int(my_snake.first_segment.xcor()) < -750:
        game_over = Over()
        game_start = False
    elif int(my_snake.first_segment.ycor()) > 750 or int(my_snake.first_segment.ycor()) < -750:
        game_over = Over()
        game_start = False

    for segment in my_snake.segment_list[1:]:
        if my_snake.first_segment.distance(segment) < 10:
            game_start = False
            game_over = Over()






screen.exitonclick()





















screen.exitonclick()












