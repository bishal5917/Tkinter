from tkinter import *

gui_var=Tk()

# widthxheight
gui_var.geometry("950x484")
gui_var.title("My Project")

gui_var.minsize(200,100)

gui_var.maxsize(900,1000)

var_2=Label(text="Library Management System",bg="light blue",fg="dark green",
                   borderwidth=3,padx=484,pady=4,font=("helvetica",15,"bold"))
var_2.pack()

#adding photo
photo=PhotoImage(file="libpng.PNG")
var2_label=Label(image=photo)
var2_label.pack()

gui_var.mainloop()

