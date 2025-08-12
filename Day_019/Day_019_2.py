from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=400,height=500)
user_bet = screen.textinput("Make your bet","Choose the racer : ")

racer1 = Turtle()
racer2 = Turtle()
racer3 = Turtle()
racer4 = Turtle()
l = [racer1, racer2, racer3, racer4]

racer1.color("red")
racer2.color("green")
racer3.color("blue")

for i in l:
    i.shape("turtle")
    i.penup()

racer1.goto((-150,-90))
racer2.goto((-150,-30))
racer3.goto((-150,30))
racer4.goto((-150,90))

for i in l:
    i.pendown()

if user_bet:
    race_on = True
    race_end = False

while race_on and not race_end:
    for i in l:
        rand_distance = random.randint(1,5)
        i.forward(rand_distance)

        position = i.pos()
        if position[0] >= 150:
            race_end = True
            winner = i.color()[0]
            print(f"The Winner is {winner} turtle")
            break

if winner == user_bet:
    print("Your racer Won!!")
else:
    print("Sorry, your racer lost.")

screen.exitonclick()