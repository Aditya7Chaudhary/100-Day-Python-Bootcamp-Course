import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle = Player()

def crossing_cars():
    cars = []
    for i in range(40):
        car = CarManager()
        car.car.goto((random.randint(-300,300),random.randint(-240,240)))
        cars.append(car)

    return cars

cars = crossing_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars:
        car.move()
        car.car_loop()
        x,y = car.car.pos()
        if turtle.clash(x,y):
            screen.exitonclick()
    
    screen.onkeypress(turtle.move,"Up")
    screen.update()

    if turtle.finish():
        for car in cars:
            car.deleting_car()
        cars = crossing_cars()
        for car in cars:
            car.car.speed(0)

screen.exitonclick()