from tkinter import *
import tkinter.messagebox as tmsg

def b():
    print(f"Congratulations.....{a.get()} Dollars have been successfully credited to your bank account!")
    tmsg.showinfo("Account Credited!",f"Congratulations.....{a.get()} Dollars have been successfully credited to your bank account")

root=Tk()
root.geometry("600x400")
Label(root,text="           How many dollars do you want????",font="comicsansms 25 bold",fg="red").pack()
a=Scale(root, from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
a.set(15)
a.pack()

c=Frame(root).pack(pady=5)
Button(c,text="Get Dollars",command=b,pady=3).pack()
root.mainloop()