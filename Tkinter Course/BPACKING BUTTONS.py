from tkinter import *
root=Tk()
root.geometry("800x500")
def a():
    print("THIS IS BUTTON A")

def b():
    print("THIS IS BUTTON B")

def c():
     print("THIS IS BUTTON C")


f=Frame(root,bg="red",borderwidth=2,relief=SUNKEN)
f.pack(side=LEFT,anchor="nw")

b1=Button(f,bg="black",fg="black",text="KABALI",command=a)
b1.pack(side=LEFT)

b2=Button(f,bg="black",fg="black",text="KABALI",command=b)
b2.pack(side=LEFT)
root.mainloop()