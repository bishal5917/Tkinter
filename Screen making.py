from tkinter import *

root=Tk()

root.geometry("600x500")
root.title("Pinnell's calculator")
root.configure(background="black")

scrn=StringVar()
scrn.set("Start calculating")

screen=Entry(root,textvariable=scrn)
screen.pack(side=TOP,fill=X,ipadx=10,ipady=10)
root.mainloop()
