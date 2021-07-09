from tkinter import *
root=Tk()

def d():
    a.set("KABALI'S GUI IS BUSY...")
    b.update()
    import time
    time.sleep(2)
    a.set("Ready..")

root.geometry("600x450")
root.title("STSTUS BAR GUI")

a=StringVar()
a.set("Ready..")

b=Label(root,textvariable=a,bg="yellow",fg="red",anchor="w")
b.pack(fill=X,side=BOTTOM)

Button(root,text="Click Me",bg="pink",fg="red",command=d).pack()
root.mainloop()