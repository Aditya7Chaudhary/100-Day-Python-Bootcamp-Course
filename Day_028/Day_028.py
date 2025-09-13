
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

canvas = tkinter.Canvas()
tomato_image = tkinter.PhotoImage(file=r"100-Day-Python-Bootcamp-Course\Day_028\tomato.png")
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.create_image(190,140,image=tomato_image)
canvas.create_text(190,170,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.pack()


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window.mainloop()