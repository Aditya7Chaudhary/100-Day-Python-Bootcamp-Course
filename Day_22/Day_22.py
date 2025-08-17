from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Welcome to the Ping-Pong Game!!")
screen.setup(800,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

paddle1 = Paddle((-330,0))
paddle2 = Paddle((330,0))
ball = Ball()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(game_is_on)
    ball.bounce(paddle1.paddle[1],paddle2.paddle[1])

    screen.onkeypress(paddle1.go_up,'w')
    screen.onkeypress(paddle1.go_down,'s')
    screen.onkeypress(paddle2.go_up,'Up')
    screen.onkeypress(paddle2.go_down,'Down')

    if ball.ball_hit_side() == True:
        ball.ball.goto((0,0))

screen.exitonclick()
