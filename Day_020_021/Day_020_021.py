from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(1000,500)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
score = 0

snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    if food.food_eaten(snake.segments[0].pos()):
        score += 1
        scoreboard.highscore_check(score)
        scoreboard.update_score(score)
        snake.add_tail()
    if snake.wall_hit():
        score = scoreboard.highscore_check(score) 
        snake.snake_reset()
    if snake.hit_tail():
        score = scoreboard.highscore_check(score)
        snake.snake_reset()


    screen.update()
    time.sleep(0.1)
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    snake.move()

screen.exitonclick()