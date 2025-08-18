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
scoreboard = Scoreboard()
screen.update()

def crossing_cars():
    cars = []
    for i in range(40):
        car = CarManager()
        car.car.goto((random.randint(-300,300),random.randint(-240,240)))
        cars.append(car)

    return cars

cars = crossing_cars()
level = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars:
        car.move()
        car.car_loop()
        x,y = car.car.pos()
        """if turtle.clash(x,y):
            game_is_on = False"""
    
    screen.onkeypress(turtle.move,"Up")
    screen.update()
    
    if turtle.win() and level == 2:
        for car in cars:
            car.deleting_car()
        turtle.turtle.hideturtle()
        scoreboard.win()
        game_is_on = False

    elif turtle.finish() and level == 1:
        for car in cars:
            car.deleting_car()
        cars = crossing_cars()
        for car in cars:
            car.car.speed(0)
        scoreboard.level_2()
        level += 1

screen.exitonclick()