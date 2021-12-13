from tkinter import *

gui_var=Tk()

# widthxheight
gui_var.geometry("950x484")

gui_var.minsize(200,100)

gui_var.maxsize(900,1000)

var_2=Label(text="Library Management System")
var_2.pack()

gui_var.mainloop()