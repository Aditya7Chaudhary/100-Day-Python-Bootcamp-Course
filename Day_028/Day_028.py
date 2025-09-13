
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


import tkinter

window = tkinter.Tk()
window.title("Pomodora")
window.config(padx=50,pady=50,bg=YELLOW)

label = tkinter.Label(text="Time on the clock",font=(FONT_NAME,30,"normal"),bg=YELLOW,fg=GREEN)

canvas = tkinter.Canvas()
tomato_image = tkinter.PhotoImage(file=r"100-Day-Python-Bootcamp-Course\Day_028\tomato.png")
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.create_image(190,110,image=tomato_image)
canvas.create_text(190,140,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")

start_button = tkinter.Button(text="Start")
reset_button = tkinter.Button(text="Reset")

label.grid(column=0,row=0,columnspan=3)
canvas.grid(column=0,row=1,columnspan=3)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()