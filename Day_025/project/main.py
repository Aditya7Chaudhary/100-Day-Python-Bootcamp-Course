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
score_changer.write(f"You have guessed {score}/50",font = ("Arial",10,"bold"))
states_guessed = []


data = pandas.read_csv(r"100-Day-Python-Bootcamp-Course\Day_025\project\50_states.csv")
for i in range(len(data)):
    if score == 50:
        score_changer.goto(0,0)
        score_changer.color('red')
        score_changer.clear()
        score_changer.write(f"You have guessed all 50/50 states.\n                   You Win!!",align="center",font = ("Arial",20,"bold"))
        break

    guess = screen.textinput(f"Your guess","Enter the US state name")
    states = data.state.to_list()
    guess = guess.capitalize()

    if guess in states:
        state_data = data[data.state == guess]
        pointer.goto(int(state_data.x),int(state_data.y))
        pointer.dot(10,"blue")
        score += 1
        score_changer.clear()
        score_changer.write(f"You have guessed {score}/50",font = ("Arial",10,"bold"))
        states_guessed.append(guess)
    else:
        score_changer.goto(0,0)
        score_changer.color('red')
        score_changer.clear()
        score_changer.write(f"You Guessed {score}/50",align="center",font = ("Arial",20,"bold"))
        break

states_not_guessed = data.state.to_list()
for i in states_guessed:
    if i in states_not_guessed:
        states_not_guessed.remove(i)

df = pandas.DataFrame(states_not_guessed)
df.to_csv(r"100-Day-Python-Bootcamp-Course\Day_025\project\States-to-learn.csv")
screen.exitonclick()