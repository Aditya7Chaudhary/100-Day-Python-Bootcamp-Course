COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.car = Turtle()
        car = self.car
        car.penup()
        car.shape('square')
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.speed(6)
        car.shapesize(1,2)
    
    def move(self):
        self.car.forward(STARTING_MOVE_DISTANCE)
    
    def car_loop(self):
        x,y = self.car.pos()
        if x <= -300:
            self.car.goto((300,y))

    def deleting_car(self):
        self.car.hideturtle()