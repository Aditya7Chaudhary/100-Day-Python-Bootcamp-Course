
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
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


# Global variable to track the timer state
timer_running = False

def clicking_of_start_button():
    global timer_running, current_time
    if not timer_running:
        start_button.config(text="Stop")
        timer_running = True
        count_down(current_time // 60, current_time % 60, text_id)
    else:
        count_down_stop(current_time // 60, current_time % 60)

def count_down(min, sec, text_id):
    global timer_running, current_time
    
    # Only continue if timer is still running
    if not timer_running:
        canvas.delete(text_id)
        return
        
    # Update the display
    canvas.delete(text_id)
    text_id = canvas.create_text(190, 140, text=f"{min:02d}:{sec:02d}", 
                                font=(FONT_NAME, 30, "bold"), fill="white")
    
    # Check if time is up
    if min == 0 and sec == 0:
        timer_running = False
        start_button.config(text="Start")
        # Add your completion logic here (check marks, etc.)
        return
    
    # Calculate next time values
    if sec == 0:
        next_min = min - 1
        next_sec = 59
    else:
        next_min = min
        next_sec = sec - 1
        
    # Store current time for pause/resume
    current_time = next_min * 60 + next_sec
    
    # Schedule next update
    window.after(1000, count_down, next_min, next_sec, text_id)

def count_down_stop(min, sec):
    global timer_running, current_time
    timer_running = False
    current_time = min * 60 + sec
    start_button.config(text="Start")

def reset_timer():
    global timer_running, current_time,text_id
    timer_running = False
    current_time = WORK_MIN * 60
    canvas.delete(text_id)
    text_id = canvas.create_text(190, 140, text=f"{current_time//60:02d}:{current_time%60:02d}", 
                                font=(FONT_NAME, 30, "bold"), fill="white")
    start_button.config(text="Start")

def break_time():
    global current_time
    if current_time == 0:
        current_time = SHORT_BREAK_MIN*60
        canvas.delete(text_id)
        text_id = canvas.create_text(190, 140, text=f"{current_time//60:02d}:{current_time%60:02d}", 
                                    font=(FONT_NAME, 30, "bold"), fill="white")


# Fixed button commands - no parentheses and no parameters in the command reference
start_button = tkinter.Button(text="Start", command=clicking_of_start_button)
reset_button = tkinter.Button(text="Reset", command=reset_timer)

check_mark = tkinter.Label(text=" ",bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))

label.grid(column=0,row=0,columnspan=3)
canvas.grid(column=0,row=1,columnspan=3)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)
check_mark.grid(column=1,row=3)

window.mainloop()