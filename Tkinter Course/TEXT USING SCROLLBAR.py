from tkinter import *
root=Tk()
root.geometry("1500x1500")
root.title("This is KABALI'S GUI!!!!!")

s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)

a=Text(root,bg="yellow",fg="red",borderwidth=5,relief=GROOVE,yscrollcommand=s.set)
a.pack(fill="both",padx=10)
s.config(command=a.yview)

root.mainloop()