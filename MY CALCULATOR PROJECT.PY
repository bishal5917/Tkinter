from tkinter import *

root=Tk()

root.geometry("600x500")
root.title("Pinnell's calculator")
# root.configure(background="black")

# making interactive screen
scrn=StringVar()
scrn.set("Start calculating")

screen=Entry(root,textvariable=scrn)
screen.pack(side=TOP,fill=X,ipadx=10,ipady=10)

# ADDING BUTTONS
frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="0",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="1",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="2",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="3",padx=10,pady=10)
but9.pack()
frm_var.pack()

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="4",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="5",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="6",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="7",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="8",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

frm_var=Frame(root,bd=3,bg="dark blue")
but9=Button(frm_var,text="9",padx=10,pady=10)
but9.pack()
frm_var.pack(side=LEFT)

root.mainloop()