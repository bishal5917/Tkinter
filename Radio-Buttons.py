from tkinter import *

root=Tk()

var=IntVar()
def handler():
    print(var.get())

Label(root,text="What is your Fav anime ?").pack()

radio=Radiobutton(root,text="AOT",padx=14,pady=10,variable=var,value=1).pack()

radio=Radiobutton(root,text="FMAB",padx=10,pady=13,variable=var,value =2).pack()

Button(root,text="Select Now",command=handler).pack()


root.mainloop()
