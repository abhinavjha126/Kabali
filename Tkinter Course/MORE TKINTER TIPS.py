from tkinter import *
root=Tk()
root.geometry("600x450")
root.title("KABALI'S GUI")
root.wm_iconbitmap("2.png")
root.configure(background="yellow")

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
print(f"{width}x{height}")
Button(root,text="CLOSE",font="comicsansms 15 bold",command=root.destroy).pack(pady=10)
root.mainloop()