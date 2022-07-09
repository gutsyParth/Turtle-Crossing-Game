from turtle import Turtle
import random

class CarManager(Turtle):
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    lev=0
    cars=[]
    def __init__(self):
        super().__init__()
        

    def create(self,pos):
        r=random.randint(1,6)
        if r==1:
            self.shape("square")
            self.color(random.choice(self.COLORS))
            self.shapesize(stretch_len=2,stretch_wid=1)
            self.penup()
            self.setpos(pos[0],pos[1])
            self.cars.append(self)
    
    def move(self):
        for c in self.cars:
            c.backward(self.STARTING_MOVE_DISTANCE)
        
    def level_up(self,i):
        self.STARTING_MOVE_DISTANCE=self.STARTING_MOVE_DISTANCE+i*2

        
     

    


    
