from turtle import Turtle, Screen
screen = Screen()

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

    def add_tail(self):
        screen.tracer(0)
        screen.update()
        self.s = Turtle()
        i = self.s
        i.shape("square")
        i.color('white')
        i.penup()

        e = self.segments[-1]
        if e.heading == 0:
            i.goto((e.pos()[0]-20,e.pos()[1]))
        elif e.heading == 90:
            i.goto((e.pos()[0],e.pos()[1]-20))
        elif e.heading == 180:
            i.goto((e.pos()[0]+20,e.pos()[1]))
        elif e.heading == 270:
            i.goto((e.pos()[0],e.pos()[1]+20))

        self.segments.append(i)
        screen.update()

    def wall_hit(self):
        x,y = self.segments[0].pos()
        if x > 500 or x < -500 or y > 250 or y < -250:
            return True
        
    def hit_tail(self):
        x,y = self.segments[0].pos()
        for i in self.segments:
            if i == self.segments[0]:
                continue
            if i.pos() == (x,y):
                return True                

    def snake_reset(self):
        for seg in self.segments:
            seg.hideturtle()
            del seg
        self.segments = []
        self.create_snake()

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