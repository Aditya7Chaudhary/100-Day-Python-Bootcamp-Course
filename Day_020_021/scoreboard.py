from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0,230))
        self.write(f"Score is : {0}",align="center",font=("Arial",10,"bold"))
    
    def update_score(self,score):
        self.clear()
        self.write(f"Score is : {score}",align="center",font=("Arial",10,"bold"))