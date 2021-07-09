from tkinter import *
root=Tk()
root.geometry("600x450")
root.title("THIS IS A GUI")

s=Scrollbar(root)
s.pack(fill=Y,side=RIGHT)

a=Listbox(root,bg="yellow",fg="red",yscrollcommand=s.set)
a.pack(fill="both",padx=22,pady=10)
s.config(command=a.yview)

for i in range(1,33):
    a.insert(ACTIVE,f"ITEM {i}")
root.mainloop()
