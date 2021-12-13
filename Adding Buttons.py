from tkinter import *

gui_var = Tk()

# widthxheight
gui_var.geometry("950x484")
gui_var.title("Software Engineering Project")

gui_var.minsize(200, 100)

gui_var.maxsize(900, 1000)

var_2 = Label(text="Library Management System", bg="light blue", fg="dark green",
                   borderwidth=3, padx=484, pady=4, font=("helvetica", 15, "bold"))
var_2.pack()

# adding photo
photo = PhotoImage(file="libpng.PNG")
var2_label = Label(image=photo)
var2_label.pack()

label_2 = Label(text="Welcome To Our Library",
                font=("italics", 20, "bold"), bg="pink")
label_2.pack()

label_3 = Label(text="Enter Your Name : ", fg="dark green",
                font=("italics", 15, "bold"), padx=12)
label_3.pack(side="left", fill="x", anchor="ne")

label_4 = Label(text="Book you want to borrow/Return : ",
                fg="dark green", font=("italics", 15, "bold"))
label_4.pack(side="left", fill="y", anchor="s")
"""
namevar=StringVar()
bookvar=StringVar()

nameentry=Entry(label_3,textvariable=namevar)
bookentry=Entry(label_4,textvariable=bookvar)

nameentry.pack(anchor="nw")
bookentry.pack(anchor="nw")
"""

# defining frames for button
frm_var = Frame(gui_var, bd=4, padx=13)
frm_var.pack(side="bottom", anchor="ne")
# defining function for button action


def borrowbook():
    print("You are about to borrow a book")


def returnbook():
    print("You are about to return a book")


# defining button
b1 = Button(frm_var, text="BORROW", bg="light blue", fg="dark red", padx=30, pady=10,
            font=("italics", 15, "bold"), command=borrowbook)
b1.pack(side="left")

b2 = Button(frm_var, text="RETURN", bg="light blue", fg="black", padx=30, pady=10,
            font=("italics", 15, "bold"), command=returnbook)
b2.pack()

gui_var.mainloop()
