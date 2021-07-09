from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untilted-Notepad")
    file=None
    text.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file== None:
        file=asksaveasfilename(initialfile="Untilted.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file = None
        else:
            #Save as a New File
            f=open(file,"w")
            f.write(text.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")
    else:
        #Save the File
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad","Notepad By KABALI")

if __name__ == '__main__':
    #BASIC TKINTER SETUP
    root=Tk()
    root.title("Untilted-Notepad")
    root.wm_iconbitmap("1.png")
    root.geometry("644x788")

    #ADD TEXT AREA
    text=Text(root,font="lucida 13 bold",bg="yellow")
    file=None
    text.pack(fill=BOTH, expand=TRUE)

    #Lets Create a Menu Bar
    Menubar=Menu(root)

    #Filemenu Starts
    Filemenu=Menu(Menubar,tearoff=0)
    #To open a new File
    Filemenu.add_command(label="New",command=newFile)
    #To Open Already Existing File
    Filemenu.add_command(label="Open",command=openFile)
    #To Save a Current File
    Filemenu.add_command(label="Save",command=saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=Filemenu)
    root.config(menu=Menubar)
    # Filemenu Ends

    # Editmenu Starts
    Editmenu = Menu(Menubar, tearoff=0)
    # To give a feature of cut
    Editmenu.add_command(label="Cut", command=cut)
    # To give a feature of cut
    Editmenu.add_command(label="Copy", command=copy)
    # To give a feature of cut
    Editmenu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit", menu=Editmenu)
    root.config(menu=Menubar)
    # Editmenu Ends

    #Helpmenu Starts
    Helpmenu = Menu(Menubar, tearoff=0)
    # To give a feature of search
    Helpmenu.add_command(label="About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=Helpmenu)
    root.config(menu=Menubar)

    # Adding Scrollbar
    s = Scrollbar(text)
    s.pack(side=RIGHT, fill=Y)
    s.config(command=text.yview)
    text.config(yscrollcommand=s.set)

    root.mainloop()