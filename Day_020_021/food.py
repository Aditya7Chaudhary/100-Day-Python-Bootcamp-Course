import random
from turtle import Turtle

class Food():
    def __init__(self):
        self.food = Turtle()
        self.food.hideturtle()
        self.food.penup()

        self.x = random.randrange(-480,480,20)
        self.y = random.randrange(-220,220,20)
        self.food.goto(self.x,self.y)
        self.food.pendown()
        self.food.dot(5,'white')
        self.food.penup()
    
    def food_eaten(self,position):
        if abs(position[0] - self.food.pos()[0]) < 10 and abs(position[1] - self.food.pos()[1]) < 10:
            self.food.clear()
            self.x = random.randrange(-480,480,20)
            self.y = random.randrange(-220,220,20)
            self.food.goto(self.x,self.y)
            self.food.pendown()
            self.food.dot(5,'white')
            self.food.penup()
            return True
            

