from tkinter import *

gui_var = Tk()

# widthxheight
gui_var.geometry("950x484")
gui_var.title("Software Engineering Project")

gui_var.minsize(200, 100)

gui_var.maxsize(900, 1000)

var_2 = Label(text="Library Management System", bg="light blue", fg="dark green",
                   borderwidth=3, padx=484, pady=4, font=("helvetica", 15, "bold"))
var_2.grid()

# adding photo
photo = PhotoImage(file="libpng.PNG")
var2_label = Label(image=photo)
var2_label.grid()

label_2 = Label(text="Welcome To Our Library",
                font=("italics", 20, "bold"), bg="pink")
label_2.grid()

# grid defining
name_label=Label(gui_var,text="Enter Your Name : ",fg="dark blue",bg="light blue")
name_label.grid()

book_label=Label(gui_var,text="Name of book you want to borrow/return : ",fg="dark blue",bg="light blue")
book_label.grid()

# defining frames for button
frm_var = Frame(gui_var, bd=4, padx=13)
frm_var.grid()
# defining function for button action


def borrowbook():
    print("You are about to borrow a book")


def returnbook():
    print("You are about to return a book")


# defining button
b1 = Button(frm_var, text="BORROW", bg="cyan", fg="dark red", padx=30, pady=10,
            font=("italics", 15, "bold"), command=borrowbook)
b1.pack(side="left")

b2 = Button(frm_var, text="RETURN", bg="cyan", fg="purple", padx=30, pady=10,
            font=("italics", 15, "bold"), command=returnbook)
b2.pack()

gui_var.mainloop()
