import tkinter

class MileToKilometer:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Mile to Kilometer Converter")
        self.window.minsize(200,200)
        self.window.config(padx=50,pady=50)

        self.label_mile = tkinter.Label(text="Mile :")
        self.label_mile.config(padx=10)
        self.label_mile.grid(column=0,row=0)

        self.input_mile = tkinter.Entry()
        self.input_mile.grid(columnspan=2,column=1,row=0)

        self.button = tkinter.Button(text="Convert",command=self.convert)
        self.button.grid(column=1,row=1)
        self.button.config(pady=10)

        self.label_kilo = tkinter.Label(text="Kilo :")
        self.label_kilo.config(padx=10)
        self.label_kilo.grid(column=0,row=2)

        self.input_kilo = tkinter.Entry()
        self.input_kilo.grid(columnspan=2,column=1,row=2)

        self.window.mainloop()
    
    def convert(self):
        mile = self.input_mile.get()
        kilo  = int(mile)*1.609344
        self.input_kilo.delete(0,tkinter.END)
        self.input_kilo.insert(0,string=str(kilo))
        

converter = MileToKilometer()