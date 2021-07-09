from tkinter import *
import tkinter.messagebox as tmsg

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("650x400")
        self.title("THIS IS KABALI'S GUI")

    def status(self):
        self.a=StringVar()
        self.a.set("Ready..")
        self.b=Label(self,textvariable=self.a,font="comicsansms 19 bold",bg="yellow",fg="red",anchor="w")
        self.b.pack(side=BOTTOM,fill=X)

    def y(self):
        print("Button Pressed!")
        self.b = tmsg.showinfo("Button Pressed", "Congratulations!!....Button has been pressed")

    def button(self):
        self.button=Button(self,text="Click Me",fg="black",font="comicsansms 10 bold",command=self.y)
        self.button.pack(pady=10)

if __name__ == '__main__':
    window=GUI()
    window.status()
    window.button()
    window.mainloop()