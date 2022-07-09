from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-280,260)

    def score_update(self,lev):
        self.clear()
        self.write(f"Level: {lev}",font=FONT)
