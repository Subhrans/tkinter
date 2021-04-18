from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("MEnu Bar")
root.geometry("800x400+200+100")
root.config(bg="#262626")


def test():
    msg.showinfo("File test", "You Clicked to file")


# First Menu
Mymenu = Menu(root)
Mymenu.add_command(label="File", command=test)

#  Own Configuration menu
top_menu = Menu(Mymenu, tearoff=0)


def navigate_menu():
    top_menu.add_command(label="Tools windows")
    top_menu.add_command(label="Run code")
    top_menu.add_separator()
    top_menu.add_command(label="Debug")
    Mymenu.add_cascade(menu=top_menu, label="Navigate")


def findWhat():
    findwhat = Menu(Mymenu)
    findwhat.add_command(label="find a character")
    findwhat.add_command(label="find word")
    return findwhat


def Edit_menu():
    editMenu = Menu(Mymenu, tearoff=0)
    editMenu.add_command(label="Save")
    editMenu.add_cascade(label="find", menu=findWhat())
    Mymenu.add_cascade(menu=editMenu, label="Edit")


root.config(menu=Mymenu)
navigate_menu()
Edit_menu()

root.mainloop()
