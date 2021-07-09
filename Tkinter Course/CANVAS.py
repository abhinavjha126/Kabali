from tkinter import *
root=Tk()
width1=800
height1=400
root.geometry(f"{width1}x{height1}")
a=Canvas(root,width=width1,height=height1)
a.pack()
c=a.create_rectangle(0,0,800,400,fill="red")
b=a.create_line(0,0,800,400)
root.mainloop()