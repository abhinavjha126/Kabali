from tkinter import *
def c():
    print(f"THE USERNAME IS: {a.get()}")
    print(f"THE PASSWORD IS: {b.get()}")
root=Tk()
root.geometry("655x333")
user=Label(root,text="USERNAME")
password=Label(root,text="PASSWORD")
user.grid()
password.grid()

a=StringVar()
b=StringVar()

userentry=Entry(root,text=a)
passentry=Entry(root,text=b)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(root,text="Submit",command=c).grid()

root.mainloop()