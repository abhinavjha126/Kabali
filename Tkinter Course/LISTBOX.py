from tkinter import *
i=0
def d():
    global i
    a.insert(ACTIVE,f"{i}")
    i+=1

root=Tk()
root.geometry("600x450")
root.title("THIS IS A GUI")
a=Listbox(root,bg="yellow")
a.pack()
a.insert(END,"First Item of Our Listbox")

Button(root,text="Click Me",command=d).pack()
root.mainloop()