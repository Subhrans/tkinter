from tkinter import *
from tkinter.ttk import Separator

# ---- initialize tk class ----

root = TkVersion  # it prints tkinter version which is 8.6
print(root)


class Basic:
    def __init__(self, root, **kwargs):
        self.root = root
        self.title = kwargs['title']
        self.root.title(self.title)
        self.w = self.root.winfo_screenwidth()
        self.h = self.root.winfo_screenheight()
        self.root.geometry(f"{self.w}x{self.h}")
        self.root.config(bg="#555")


def entry_data():
    display_lbl.config(bg="#f5d97a",
                       text=txt1.get(),
                       font=("bell mt", 30, "bold"),

                       )


root = Tk()
b1 = Basic(root, title="2nd tkinter tutorial")
lbl1 = Label(root, bg="#04a790").pack(side=LEFT, expand=1, fill=BOTH)
lbl2 = Label(root, bg="#80baeb").pack(side=RIGHT, expand=1, fill=BOTH)
frame1 = Frame(root, bg="red").place(x=b1.h // 3, y=b1.h // 4, relwidth=0.6, height=400)
lbl4 = Label(frame1, bg="#f5d97a").place(x=b1.h // 3, y=b1.h // 4, relwidth=0.6, height=400)
lbl3 = Label(lbl2, text="Username",
             font=("times new roman", 30, "bold"),
             pady=100,
             bg="#f5d97a",
             fg="#fff"
             ).place(x=b1.h // 2, y=b1.h // 4)
txt1 = Entry(root, bg="#f5d97a", font=("times new roman", 20, "bold"), relief="flat", bd=2)
txt1.place(x=b1.h, y=b1.h // 3)
s1 = Label(root, bg="white").place(x=b1.h, y=b1.h // 2.6, height=4, width=200)
btn1 = Button(root, text="Show",
              font=("bell mt", 30, "bold"),
              bg="gray",
              fg="white",
              cursor="hand2",
              activebackground="#80baeb",
              activeforeground="#04a790",
              command=entry_data
              ).place(x=b1.h // 2, y=b1.h // 2)

display_lbl = Label(root,bg="#f5d97a")
display_lbl.place(x=b1.h, y=b1.h // 2)
root.mainloop()
