from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(1000,500)
screen.tracer(0)
screen.listen()

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    snake.move()

screen.exitonclick()