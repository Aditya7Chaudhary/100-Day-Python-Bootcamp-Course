from turtle import Turtle, Screen

screen = Screen()
player = Turtle()
screen.listen()

def move_forward():
    player.forward(10)

def move_backward():
    player.backward(10)

def turn_clockwise():
    new_heading = player.heading() - 10
    player.setheading(new_heading)

def turn_anticlockwise():
    new_heading = player.heading() + 10
    player.setheading(new_heading)

def clear():
    player.clear()
    player.penup()
    player.home()
    player.pendown()


def sketch():
    screen.onkeypress(move_forward, "w")
    screen.onkeypress(move_backward, "s")
    screen.onkeypress(turn_anticlockwise, "a")
    screen.onkeypress(turn_clockwise,"d")
    screen.onkey(clear,"c")

sketch()
screen.exitonclick()