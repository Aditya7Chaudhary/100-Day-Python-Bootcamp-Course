
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

label = tkinter.Label(text="Timer",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN,pady=20)

canvas = tkinter.Canvas()
tomato_image = tkinter.PhotoImage(file=r"100-Day-Python-Bootcamp-Course\Day_028\tomato.png")
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.create_image(190,110,image=tomato_image)

current_time = WORK_MIN*60
text_id = canvas.create_text(190,140,text=f"{current_time//60:02d}:{current_time%60:02d}",font=(FONT_NAME,30,"bold"),fill="white")


def clicking_of_start_button(current_time):
    start_button.config(text="Stop")
    count_down(current_time//60,current_time%60,text_id)

def count_down(min,sec,text_id):
    start_button.config(command=lambda:count_down_stop(min,sec))
    if start_button.cget("text") == "Stop":
        canvas.delete(text_id)
        if sec == 0:
            min -= 1
            sec = 59
        text_id = canvas.create_text(190,140,text=f"{min:02d}:{sec:02d}",font=(FONT_NAME,30,"bold"),fill="white")
        window.after(1000,count_down,min,sec-1,text_id)

def count_down_stop(min,sec):
    global current_time
    current_time = min*60 + sec
    start_button.config(text="Start",command=lambda:clicking_of_start_button(current_time))


start_button = tkinter.Button(text="Start",command=clicking_of_start_button(current_time))

reset_button = tkinter.Button(text="Reset")

check_mark = tkinter.Label(text=" ",bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))

label.grid(column=0,row=0,columnspan=3)
canvas.grid(column=0,row=1,columnspan=3)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)
check_mark.grid(column=1,row=3)

window.mainloop()