from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(600,400)
screen.tracer(0)
screen.listen()

s1 = Turtle()
s2 = Turtle()
s3 = Turtle()
segments = [s1,s2,s3]
a = 0
for i in segments:
    i.shape("square")
    i.color('white')
    i.penup()
    i.goto(a,0)
    a -= 20
    i.speed(10)

screen.update()

def turn_left():
    a=0
    while a < len(segments):
        for seg in segments:
            if seg == segments[a]:
                seg.left(90)
            seg.forward(20)
        a += 1
        

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.onkey(turn_left,'a')
    for seg in segments:
        seg.forward(20)


screen.exitonclick()