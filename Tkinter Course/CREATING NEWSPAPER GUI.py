from tkinter import *
root=Tk()
root.geometry("800x400")
root.title("WELCOME TO KABALI'S GUI")

f1=Frame(root,borderwidth=3,relief=GROOVE)
f1.pack(side=LEFT,anchor="nw")
l1=Label(f1,text="YE KABALI KA GUI HAIN BHAIYA",bg="yellow",fg="red")
l1.pack()

f2=Frame(root,borderwidth=3,relief=GROOVE)
f2.pack(side=TOP,anchor="nw",fill=X)
l2=Label(f2,text="YE PYCHARM HAIN",fg="red",bg="yellow")
l2.pack(fill=X)

f3=Frame(root,borderwidth=3,relief=GROOVE,bg="yellow")
f3.pack(side=LEFT,anchor="nw")
l3=Label(f3,text="ITS DONE",bg="yellow",fg="red")
l3.pack()

root.mainloop()