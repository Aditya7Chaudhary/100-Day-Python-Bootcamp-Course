import tkinter

class MileToKilometer:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Mile to Kilometer Converter")
        self.window.minsize(200,200)
        self.window.config(padx=50,pady=50)

        self.label = tkinter.Label(text="Mile :")
        self.label.grid(column=0,row=0)

        self.input_mile = tkinter.Entry()
        self.input_mile.grid(columnspan=2,column=1,row=0)

        self.window.mainloop()

converter = MileToKilometer()