from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore  = 0
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((0,230))
        self.write(f"Score is : {self.score} Highscore is : {self.highscore}",align="center",font=("Arial",10,"bold"))
    
    def update_score(self,score):
        self.clear()
        self.write(f"Score is : {score} Highscore is : {self.highscore}",align="center",font=("Arial",10,"bold"))
    
    def highscore_check(self,score):
        self.clear()
        if score > self.highscore:
            self.highscore = score
            self.score = 0
        self.write(f"Score is : {self.score} Highscore is : {self.highscore}",align="center",font=("Arial",10,"bold"))
        return self.score