from tkinter import *
import tkinter.messagebox as tmsg

def d():
    print(f"Congratulations.....Your order of {a.get()} has been placed successfully!")
    tmsg.showinfo("Order Placed",f"Congratulations.....Your order of {a.get()} has been placed successfully!")

root=Tk()
root.geometry("600x400")
root.title(" KABALI'S KHANA SHOP")
Label(root,text="WHAT WOULD YOU LIKE TO ORDER?????",font="comicsansms 30 bold",fg="red").pack()

a=StringVar()
a.set("Kabali")
b=Radiobutton(root,text="Dosa",variable=a,value="Dosa").pack(anchor="w")
b=Radiobutton(root,text="Idli",variable=a,value="Idli").pack(anchor="w")
b=Radiobutton(root,text="Paratha",variable=a,value="Paratha").pack(anchor="w")
b=Radiobutton(root,text="Chowmein",variable=a,value="Chowmein").pack(anchor="w")

c=Button(root,text="Place Order",fg="green",command=d).pack()

root.mainloop()