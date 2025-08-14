from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        self.s1 = Turtle()
        self.s2 = Turtle()
        self.s3 = Turtle()
        self.segments = [self.s1,self.s2,self.s3]
        a = 0
        for i in self.segments:
            i.shape("square")
            i.color('white')
            i.penup()
            i.goto(a,0)
            a -= 20


    def move(self):
        i = 1
        seg = self.segments
        x_cod, y_cod = seg[0].pos()
        seg[0].forward(20)
        while i < len(seg):
            new_x_cod, new_y_cod = seg[i].pos()
            seg[i].goto(x_cod,y_cod)
            x_cod = new_x_cod
            y_cod = new_y_cod
            i += 1     

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)    