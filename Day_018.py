from turtle import Turtle, Screen
import time
import random

player = Turtle()
screen = Screen()

screen.title("Turtle Graphics Window")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600, startx=0, starty=0)

player.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(4):
    player.forward(100)
    player.right(90.0)

player.clear()
time.sleep(0.5)

for i in range(10):
    player.forward(10)
    player.penup()
    player.forward(10)
    player.pendown()

screen.reset()
time.sleep(0.5)

for i in range(3,11):
    deg = (180*(i-2))/i
    player.pencolor(random.choice(colours))
    for j in range(i):
        player.forward(100)
        player.right(180-deg)

time.sleep(0.5)
screen.reset()

random_walk = [0,1]
player.speed(10)
for i in range(200):
    player.pencolor(random.choice(colours))
    player.forward(20)
    a = random.choice(random_walk)
    if a==0:
        player.left(90)
    else:
        player.right(90)

time.sleep(0.5)
screen.reset()

player.speed(0)
for i in range(180):
    player.pencolor(random.choice(colours))
    player.circle(100)
    player.right(2)

screen.exitonclick()