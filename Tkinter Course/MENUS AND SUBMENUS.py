from tkinter import *
root=Tk()
root.title("THIS IS A GUI")
root.geometry("700x500")

def b1():
    print("HE IS THE MALE HEAD OF THE FAMILY: PAPA")
def r1():
    print("SHE IS THE FEMALE HEAD OF OUR FAMILY: MOM")
def a1():
    print("SHE IS THE BACKBONE OF OUR FAMILY....MY PARENT'S STRENGTH: JAYA DI")
def p1():
    print("SHE IS THE SWEETEST SISTER TO WHOM I HAVE TO CARE THE MOST: PRIYA DI")
def a2():
    print("THIS IS ME...MY FAMILY'S PRIDE: KABALI")

a=Menu(root)

b=Menu(a,tearoff=0)
b.add_command(label="Bateshwar",command=b1)
b.add_command(label="Ranju",command=r1)
b.add_command(label="Aparna",command=a1)
b.add_separator()
b.add_command(label="Priya",command=p1)
b.add_command(label="Abhinav",command=a2)
root.config(menu=a)
a.add_cascade(label="Family Members",menu=b)

root.mainloop()