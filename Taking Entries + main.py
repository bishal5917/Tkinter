from tkinter import *
import tkinter.messagebox as tmsg

gui_var = Tk()

# widthxheight
gui_var.geometry("900x484")
gui_var.title("Software Engineering Project")
gui_var.iconbitmap("my project icon.ico")
gui_var.configure(background="black")

gui_var.minsize(200, 100)

gui_var.maxsize(900, 1000)

var_2 = Label(text="Library Management System", bg="light blue", fg="dark green",
                   borderwidth=8, padx=15, pady=8, font=("helvetica", 15, "bold"))
var_2.grid(row=1, column=1)
"""
# adding photo
photo = PhotoImage(file="libpng.PNG")
var2_label = Label(image=photo)
var2_label.grid(column=3)
"""
photo = PhotoImage(file="libpng.png")
logophoto = Label(image=photo)
logophoto.grid(row=2, column=1)

label_2 = Label(text="Welcome To Our Library,Please Enter the Details Here",
                font=("italics", 20, "bold"), bg="pink")
label_2.grid(row=3, column=1)

# labels to take input defining
name_label = Label(gui_var, text="Your Full Name : ", padx=21,
                   pady=10, fg="dark blue", bg="light blue")
name_label.grid(row=4, column=1)

book_label = Label(gui_var, text="Name of book you want to borrow/return : ",
                   padx=21, pady=10, fg="dark blue", bg="light blue")
book_label.grid(row=5, column=1)

# variables to take entry defining
namevar = StringVar()
bookvar = StringVar()

nameentry = Entry(gui_var, textvariable=namevar)
bookentry = Entry(gui_var, textvariable=bookvar)

nameentry.grid(row=4, column=2)
bookentry.grid(row=5, column=2)

# defining frames for button
frm_var = Frame(gui_var, bd=4, padx=13)
frm_var.grid(column=1)
# defining function for button action


def borrowbook():
    print("You are about to borrow a book")
    tmsg.showinfo(title="Borrowed", message="Book Borrowed Successfully ! ")


def returnbook():
    print("You are about to return a book")
    tmsg.showinfo(title="Returned", message="Book Returned Successfully ! ")


# defining button
b1 = Button(frm_var, text="BORROW", bg="cyan", fg="dark red", padx=30, pady=10,
            font=("italics", 15, "bold"), command=borrowbook)
b1.grid(row=5, column=1)

b2 = Button(frm_var, text="RETURN", bg="cyan", fg="purple", padx=30, pady=10,
            font=("italics", 15, "bold"), command=returnbook)
b2.grid(row=5, column=2)

gui_var.mainloop()
