from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Welcome to the Ping-Pong Game!!")
screen.setup(800,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

paddle1 = Paddle((-330,0))
paddle2 = Paddle((330,0))

game_is_on = True
while game_is_on:
    screen.update()
    screen.onkey(paddle1.go_up,'w')
    screen.onkey(paddle1.go_down,'s')
    screen.update()
    screen.onkey(paddle2.go_up,'Up')
    screen.onkey(paddle2.go_down,'Down')

screen.exitonclick()
