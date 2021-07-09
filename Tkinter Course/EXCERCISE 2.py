from tkinter import *
root=Tk()

def res():
    root.geometry(f"{c.get()}x{d.get()}")

root.geometry("1600x1000")
root.title("THIS IS KABALI'S GUI")

a1=Label(root,text="PLEASE UPDATE THE GUI WINDOW SIZE",font="cosmicsansms 40 bold",fg="red",pady=10)
a1.grid(row=0,column=4)
a=Label(root,text="PLEASE ENTER WIDTH",font="cosmicsansms 25")
a.grid(row=1,column=2)
b=Label(root,text="PLEASE ENTER HEIGHT",font="cosmicsansms 25")
b.grid(row=2,column=2)

c=StringVar()
d=StringVar()

c1=Entry(root,text=c)
c1.grid(row=1,column=3)
d1=Entry(root,text=d)
d1.grid(row=2,column=3)

e=Button(root,text="Submit",command=res)
e.grid(row=3,column=3)


root.mainloop()