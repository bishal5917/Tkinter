from tkinter import *

gui_var=Tk()

# widthxheight
gui_var.geometry("950x484")
gui_var.title("Software Engineering Project")

gui_var.minsize(200,100)

gui_var.maxsize(900,1000)

var_2=Label(text="Library Management System",bg="light blue",fg="dark green",
                   borderwidth=3,padx=484,pady=4,font=("helvetica",15,"bold"))
var_2.pack()

#adding photo
photo=PhotoImage(file="libpng.PNG")
var2_label=Label(image=photo)
var2_label.pack()

label_2=Label(text="Welcome To Our Library",font=("italics",20,"bold"),bg="pink")
label_2.pack()

label_3=Label(text="Enter Your Name : ",fg="dark green",font=("italics",12),padx=12)
label_3.pack(side="left",fill="x")

gui_var.mainloop()