FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('red')
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write("Level 1",align='center',font = FONT)

    def level_2(self):
        self.clear()
        self.goto(0,260)
        self.write("Level 2",align='center',font = FONT)

    def win(self):
        self.clear()
        self.goto(0,0)
        self.write("You Win",align='center',font = ("Courier", 50, "bold"))
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over",align='center',font = ("Courier", 50, "bold"))