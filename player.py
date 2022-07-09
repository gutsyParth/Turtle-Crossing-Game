from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    lev=1
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("cyan")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        if self.ycor()>=280:
            self.lev=self.lev+1
            self.goto(STARTING_POSITION)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.forward(-1*MOVE_DISTANCE)
