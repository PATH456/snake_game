from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.first_segment = self.segment_list[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def reset_snake(self):
        self.first_segment.goto((0, 0))
        self.segment_list[1].goto((-20, 0))
        self.segment_list[2].goto((-40, 0))

    def add_segment(self, pos):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment_list.append(new_segment)


    def extend(self):
        self.add_segment(self.segment_list[-1].position())


    def move(self):
        for seg_num in range(len(self.segment_list)-1, 0, -1):
            new_x = self.segment_list[seg_num - 1].xcor()
            new_y = self.segment_list[seg_num - 1].ycor()
            self.segment_list[seg_num].goto(new_x, new_y)
        self.first_segment.forward(MOVE_DISTANCE)



