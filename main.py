import time
import random
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

p=Player()
s=Scoreboard()

t=Turtle()
t.hideturtle()

game_is_on = True

l=0

while game_is_on:
    time.sleep(0.1)

    car=CarManager()
    car.create((300,random.randint(-250,250)))

    screen.onkey(p.move_up,"Up")
    screen.onkey(p.move_down,"Down")

    s.score_update(p.lev)

    for c in car.cars:
        if c.distance(p)<=20:
            game_is_on=False
            screen.clear()
            t.write(f"Game Over! \nLevel reached : {p.lev}",font=("Courier", 30, "normal"),align="center")
    
    
    car.level_up(p.lev)
    
    car.lev=p.lev
    car.move()

    screen.update()

screen.exitonclick()
