from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.speed(1)
        self.ball.setheading(random.randint(0,360))

    def move(self,game_is_on):
        if game_is_on:
            self.ball.forward(20)

    def bounce(self,paddle1,paddle2):
        x, y = self.ball.pos()
        x1,y1 = paddle1.pos()
        x2,y2 = paddle2.pos()

        prev_collision = False
        if (300 - abs(y)) < 10 and prev_collision == False:
            prev_collision == True
            theta = self.ball.heading()
            new_theta = 360.0 - theta
            self.ball.setheading(new_theta)

        if (abs(x1) - abs(x)) < 10 and (y1-20<y<y1+20 or y2-20<y<y2+20) and prev_collision == False:
            prev_collision = True
            theta = self.ball.heading()
            new_theta = 180.0 - theta
            self.ball.setheading(new_theta)

    def ball_hit_side(self):
        x, y = self.ball.pos()
        if (400 - abs(x)) < 20:
            self.ball.setheading(180+self.ball.heading())
            return True