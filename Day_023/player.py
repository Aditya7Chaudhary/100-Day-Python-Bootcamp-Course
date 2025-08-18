STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape('turtle')
        self.turtle.setheading(90)
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.shapesize(1,1)
    
    def move(self):
        self.turtle.forward(MOVE_DISTANCE)

    def finish(self):
        x,y = self.turtle.pos()
        if y >= FINISH_LINE_Y:
            self.turtle.goto(STARTING_POSITION)
            return True
    
    def win(self):
        x,y = self.turtle.pos()
        if y >= FINISH_LINE_Y:
            return True
        
    def clash(self,x,y):
        x_0,y_0 = self.turtle.pos()
        if abs(x_0 - x) < 25 and abs(y_0 - y) < 20:
            return True