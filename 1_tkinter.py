from tkinter import *

root = Tk()
root.title(string="FIRST GUI BY MY SELF")
# root.resizable(width=True,height=False)
root.config(bg="#666")
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print(w)
root.geometry(f"{w}x{h}+-8+0")
# ------------------ Grid System --------------------
# this is not responsive behavior
# label1 = Label(root,text="Text 1")
# label1.grid(row=0,column=0)
# label2 = Label(root,text="Text 2")
# label2.grid(row=0,column=1)
# label3 = Label(root,text="Text 3")
# label3.grid(row=2,column=2)

# ------------------ Pack System --------------------
# label1 = Label(root,text="Text 1")
# label1.pack()
# label2 = Label(root,text="Text 2")
# label2.pack()
# label3 = Label(root,text="Text 3")
# label3.pack()

# ------------------ Place System --------------------
# this is not responsive behavior
label1 = Label(root,text="Text 1")
label1.place(x=100,y=100)
label2 = Label(root,text="Text 2")
label2.place(x=w//2,y=h//2)   # center of full with screen
label3 = Label(root,text="Text 3")
label3.place(x=200,y=300,height=100,relwidth=0.5)
root.mainloop()