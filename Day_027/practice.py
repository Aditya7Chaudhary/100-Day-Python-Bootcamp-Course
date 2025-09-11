import tkinter

window = tkinter.Tk()
window.minsize(width=600,height=400)
window.title("My first GUI project!!")

label = tkinter.Label(text="Hello world",font=("Arial",20,"bold"))
label.pack()

def button_click():
    label.config(text="Clicked!")

button = tkinter.Button(text="Click me",command=button_click)
button.pack()

window.mainloop()