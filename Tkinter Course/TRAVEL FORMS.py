from tkinter import *
root=Tk()
root.geometry("1500x1100")
root.title("KHANA KYA KHANA HAIN????")
a=Label(root,text="BHARO FORM JO KHANA HAIN PRIYA KE B'DAY MEIN AAJ",font="comicsansms 25 bold",pady=10)
a.grid(column=6)

a=Label(root,text="Name",font="comicsansms 25 ").grid(row=1,column=0)
b=Label(root,text="Mob.No",font="comicsansms 25 ").grid(row=2,column=0)
c=Label(root,text="D.O.B",font="comicsansms 25 ").grid(row=3,column=0)
d=Label(root,text="Food Item",font="comicsansms 25 ").grid(row=4,column=0)

a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=IntVar()

b1=Entry(root,text=a1).grid(row=1,column=1)
b2=Entry(root,text=a2).grid(row=2,column=1)
b3=Entry(root,text=a3).grid(row=3,column=1)
b4=Entry(root,text=a4).grid(row=4,column=1)

b5=Checkbutton(root,text="Kuch Contribute krogi gareeb ladki??").grid(row=5,column=1)

Button(root,text="Submit to Kabali",font="comicsansms 15",pady=5).grid(row=6,column=1,padx=20)

root.mainloop()