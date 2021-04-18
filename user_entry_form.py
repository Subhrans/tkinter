from tkinter import *

root = Tk()
root.title(string="User Entry Form")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f"{w}x{h}")
background_label = Label(root, bg="#fff").pack(side=TOP, expand=1, fill=BOTH)
title_lbl=Label(root,fg="#901010",text="User Entry Form",font=("Impact",30,"bold"),bg="#fff").place(x=0,y=0,relwidth=1)
# ------------------- USername -------------------------
username_lbl = Label(root, fg="#333", bg="#fff", text="Username", font=("times new roman", 20, "bold")).place(x=w // 4,
                                                                                                              y=h // 4)
username_entry = Entry(root, fg="#fff", bg="#888", font=("bell mt", 15))
username_entry.place(x=w // 2.7, y=h // 4)
#  ------------------------- Password =======================
password_lbl = Label(root, fg="#333", bg="#fff", text="Password", font=("times new roman", 20, "bold")).place(x=w // 4,
                                                                                                              y=h // 3)
password_entry = Entry(root, fg="#fff", bg="#888", font=("bell mt", 15))
password_entry.place(x=w // 2.7, y=h // 3)
# ==================== Radio =============================
radio_btn1_value = StringVar()
radio_btn1_value.set(None)
radio_btn1 = Radiobutton(root, text="male",font=('times new roman', 20), value="male",variable=radio_btn1_value)
radio_btn1.place(x=w // 2.7, y=h // 2.5)
# radio_btn2_value = StringVar()
# radio_btn2_value.set(None)
radio_btn2 = Radiobutton(root, text="female", font=('times new roman', 20), value="female",variable=radio_btn1_value)
radio_btn2.place(x=w // 2, y=h // 2.5)

# ================ Check terms ===========================
chk_value = IntVar()
chk_btn = Checkbutton(root, font=("times new roman", 20), text="Accept the terms and condition", onvalue=1, offvalue=0,
                      variable=chk_value)
chk_btn.place(x=w // 2.7, y=h // 2.2)


def get_data():
    if chk_value.get() == 1:
        print(username_entry.get())
        print(password_entry.get())
        print(chk_value.get())
        if radio_btn1_value:
            print(radio_btn1_value.get())
        # print(radio_btn2_value.get())


submit_btn = Button(root, text="Submit", bg="#666", fg="#fff", font=("times new roman", 25), command=get_data)
submit_btn.place(x=w // 2.7, y=h // 1.8)

root.mainloop()
