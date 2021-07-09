from tkinter import *

def click(event):
    global a
    d=event.widget.cget("text")

    if d== "C":
        print(f"{b.get()} \n")
    else:
        print(d, end="")
    if d =="=":
        if a.get().isdigit():
            value=int(a.get())
        else:
            try:
                value=eval(b.get())
            except Exception as e:
                print(e)
                value="ERROR"
        a.set(value)
        b.update()
    elif d =="C":
        a.set("")
        b.update()
    else:
        a.set(a.get()+d)
        b.update()

root=Tk()
root.geometry("525x650")
root.title("CALCULATOR")
root.wm_iconbitmap("1.png")
root.configure(background="pink")

Label(root,text="KABALI,S CALCULATOR",fg="black",font="comicsansms 30 bold",bg="pink").pack(fill=X)
a=StringVar()
a.set("")
b=Entry(root,textvar=a,font="lucida 40 bold")
b.pack(fill=X,pady=5)

f1=Frame(root,bg="pink",borderwidth=4,relief=SUNKEN,pady=10)
b1=Button(f1,text="C",font="comicsansms 80 bold",fg="black",padx=20)
b1.pack(side=LEFT,padx=15)
b1.bind("<Button-1>",click)
b2=Button(f1,text="0",font="comicsansms 80 bold",fg="black",padx=20)
b2.pack(side=LEFT,padx=15)
b2.bind("<Button-1>",click)
b3=Button(f1,text="/",font="comicsansms 80 bold",fg="black",padx=30)
b3.pack(side=LEFT,padx=15)
b3.bind("<Button-1>",click)
b4=Button(f1,text="*",font="comicsansms 80 bold",fg="black",padx=30)
b4.pack(side=LEFT,padx=14)
b4.bind("<Button-1>",click)
f1.pack(fill=X)


f1=Frame(root,bg="pink",borderwidth=4,relief=SUNKEN,pady=10)
b1=Button(f1,text="9",font="comicsansms 80 bold",fg="black",padx=20)
b1.pack(side=LEFT,padx=15)
b1.bind("<Button-1>",click)
b2=Button(f1,text="8",font="comicsansms 80 bold",fg="black",padx=20)
b2.pack(side=LEFT,padx=15)
b2.bind("<Button-1>",click)
b3=Button(f1,text="7",font="comicsansms 80 bold",fg="black",padx=20)
b3.pack(side=LEFT,padx=15)
b3.bind("<Button-1>",click)
b4=Button(f1,text="-",font="comicsansms 80 bold",fg="black",padx=28)
b4.pack(side=LEFT,padx=16)
b4.bind("<Button-1>",click)
f1.pack(fill=X)

f1=Frame(root,bg="pink",borderwidth=4,relief=SUNKEN,pady=10)
b1=Button(f1,text="6",font="comicsansms 80 bold",fg="black",padx=20)
b1.pack(side=LEFT,padx=15)
b1.bind("<Button-1>",click)
b2=Button(f1,text="5",font="comicsansms 80 bold",fg="black",padx=20)
b2.pack(side=LEFT,padx=15)
b2.bind("<Button-1>",click)
b3=Button(f1,text="4",font="comicsansms 80 bold",fg="black",padx=20)
b3.pack(side=LEFT,padx=15)
b3.bind("<Button-1>",click)
b4=Button(f1,text="+",font="comicsansms 80 bold",fg="black",padx=26)
b4.pack(side=LEFT,padx=15)
b4.bind("<Button-1>",click)
f1.pack(fill=X)

f1=Frame(root,bg="pink",borderwidth=4,relief=SUNKEN,pady=10)
b1=Button(f1,text="3",font="comicsansms 80 bold",fg="black",padx=20)
b1.pack(side=LEFT,padx=15)
b1.bind("<Button-1>",click)
b2=Button(f1,text="2",font="comicsansms 80 bold",fg="black",padx=20)
b2.pack(side=LEFT,padx=15)
b2.bind("<Button-1>",click)
b3=Button(f1,text="1",font="comicsansms 80 bold",fg="black",padx=20)
b3.pack(side=LEFT,padx=15)
b3.bind("<Button-1>",click)
b4=Button(f1,text="=",font="comicsansms 80 bold",fg="black",padx=22)
b4.pack(side=LEFT,padx=15)
b4.bind("<Button-1>",click)
f1.pack(fill=X)

root.mainloop()