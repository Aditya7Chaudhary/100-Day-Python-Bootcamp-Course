import turtle
import pandas

screen = turtle.Screen()
image = r"100-Day-Python-Bootcamp-Course\Day_025\project\blank_states_img.gif"
screen.title("US states game")
screen.addshape(image)

turtle.shape(image)
pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
score_changer = turtle.Turtle()
score_changer.hideturtle()
score_changer.penup()
score_changer.goto(-300,220)
score_changer.pencolor('black')
score = 0
score_changer.write(f"Score = {score}",font = ("Arial",20,"bold"))

data = pandas.read_csv(r"100-Day-Python-Bootcamp-Course\Day_025\project\50_states.csv")
for i in range(len(data)):
    guess = screen.textinput(f"Your guess","Enter the US state name")
    if guess in data.state.to_list():
        state_data = data[data.state == guess]
        pointer.goto(int(state_data.x),int(state_data.y))
        pointer.dot(10,"blue")
        score += 1
        score_changer.clear()
        score_changer.write(f"Score = {score}",font = ("Arial",20,"bold"))
    else:
        score_changer.goto(0,0)
        score_changer.color('red')
        score_changer.clear()
        score_changer.write(f"Your Score is : {score}",align="center",font = ("Arial",20,"bold"))
        break

screen.exitonclick()