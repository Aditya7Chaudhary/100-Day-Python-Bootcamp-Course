from turtle import Turtle

class Paddle:
    def __init__(self,pos):
        t1 = Turtle()
        t2 = Turtle()
        t3 = Turtle()
        self.paddle = [t1,t2,t3]

        x,y = pos
        a = y-20

        for t in self.paddle:
            t.penup()
            t.shape('square')
            t.color('white')
            t.setheading(90)
            t.speed(0)
            t.goto(x,a)
            a += 20

    def go_up(self):
        for t in self.paddle:
            t.forward(20)
    
    def go_down(self):
        for t in self.paddle:
            t.backward(20)