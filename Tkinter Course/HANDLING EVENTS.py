from  tkinter import *
root=Tk()
def harry(event):
    print(f"The Co-Ordinate is: {event.x},{event.y}")
root.geometry("644x334")
a=Button(root,text="Click On Me")
a.pack()
a.bind("<Button-1>",harry)
a.bind("<Double-1>",quit)
root.mainloop()